from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from models import Spartan, CreateSpartanForm


@login_required
def spartan(request):
    if request.user.account.has_related_object() and request.user.spartan.spartanStatus:
        raise PermissionDenied
    confirm = []
    form = CreateSpartanForm(data=request.POST or None)
    if request.method == 'POST':
        if not request.user.account.has_related_object() and form.is_valid():
            form.instance.user = request.user
            form.save()
            form.instance.activation_email()
            confirm.append('You\'ve completed the form, '
                           'wait for admin\'s confirmation')
    return render(request, 'spartan/spartan.html', {
        'form': form,
        'confirms': confirm})


@login_required
def user(request, slug):
    current_spartan = get_object_or_404(Spartan, slug=slug)
    return render(request, 'spartan/SpartanPage.html', {
        'reviews': current_spartan.reviews,
        'spartan': current_spartan,
        'img_spartan': current_spartan.user.account.profile_image,
    })
