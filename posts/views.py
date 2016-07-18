import json
import random
import string

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from channels import Group
from haystack.forms import SearchForm

from .models import Announcement, EditPostForm, CreatePostForm
from bidding.models import CreateOfferForm
from .tasks import notify_spartans, email_user, notify_bid


@login_required
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            category = post.category
            url = post.get_absolute_url()
            messagetip = " Hi! % s , \n You successfully"\
                         "posted an announce! \n" \
                         " Title: %s ,\n Description: %s \n Address: %s \n " \
                         "Country : %s \n City: %s \n Category: %s \n" \
                         " Time : %s \n Date: %s \n " \
                         "Highest bid price: %s eur \n" \
                         " Have a nice day! - Team Spartan" % (
                             current_user.username, post.title,
                             post.description,
                             post.address,
                             post.country,  post.city,  post.category.name,
                             post.timePost, post.data, post.money)
            email_user.delay(messagetip, current_user.email,
                             "Spartan Tasks Post")
            id_hash = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(6))
            notify_spartans.delay(category.name, post.city,
                                  post.author.username,
                                  url, id_hash)
            html = """
            <a href=\"""" + url + """\" id="seen_notif_req"
            data-notification=\"""" + id_hash + """\"
            onmouseover="seen_not(this.getAttribute('data-notification'));">
            <li class="list-group-item" id=\"""" + id_hash + """\">
            <i class="fa fa-exclamation-circle icon"></i>New post in your area
            </li>
            </a>
            """
            dic = {
                'author': current_user.username,
                'html': html,
                'posts': 'post'
            }
            Group("spartans-" + category.name +
                  "-" + post.city).send({'text': json.dumps(dic)})
            return redirect(post.get_absolute_url())
    return render(request, 'posts/create_post.html', {
        'form': form})


@login_required
def post(request, slug):
    post = get_object_or_404(Announcement, slug=slug)
    form = CreateOfferForm(data=request.POST or None, post=post)
    if post.status and request.user != post.author and \
       request.user != post.spartan.user:
        raise Http404()
    confirms = []
    if request.method == 'POST':
        if request.POST.get("deletePost"):
            post.delete()
            return redirect('/')
        if form.is_valid():
            bid = form.instance
            bid.post = post
            bid.spartan = request.user.spartan
            form.save()
            receiver = post.author.username
            id_hash = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(6))
            html = """
            <a href=\"""" + post.get_absolute_url() + """\" id="seen_notif_req"
            data-notification=\"""" + id_hash + """\"
            onmouseover="seen_not(this.getAttribute('data-notification'));">
            <li class="list-group-item" id=\"""" + id_hash + """\">
            <i class="fa fa-exclamation-circle icon"></i>
            Someone bid on your post
            </li>
            </a>
            """
            dic = {
                'html': html,
                'author': bid.spartan.user.username,
                'type': 'bid'
            }
            Group("channel-" + receiver).send({
                'text': json.dumps(dic)})
            notify_bid.delay(receiver, post.get_absolute_url(), id_hash)
            confirms.append('Offer was sent')
    return render(request, 'posts/post.html', {
        'ann': Announcement.objects.filter(status=False).order_by(
            '-creation_date')[:4],
        'user': request.user,
        'post': post,
        'form': form,
        'confirms': confirms
    })


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Announcement, slug=slug, status=False)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditPostForm(request.POST or None, request.FILES or None,
                        instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/post/' + post.slug)
    return render(request, 'posts/edit_post.html', {
        'post': post,
        'form': form,
    })


@login_required
def search(request):
    form = SearchForm(request.GET)
    posts = None
    if form.data != {} and form.is_valid():
        posts = form.search()
    return render_to_response('search/search.html', {
        'posts': posts
    })
