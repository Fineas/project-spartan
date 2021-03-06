# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.

from django.test import TestCase
from django.contrib.auth.models import User

from spartans.models import Spartan
from categories.models import Category
from .forms import CreateSpartanForm
from authentication.models import Account, City, Country


class SpartanFormsTestCase(TestCase):
    def setUp(self):
        country = Country.objects.create(name="Romania")
        city = City.objects.create(name="Timisoara", country=country)
        self.user = User.objects.create_user(username="tester",
                                             email="smt@smt.com",
                                             password="top_secret")
        self.spartan = User.objects.create_user(username="testerspartan",
                                                email="smt@gmail.com",
                                                password="top_secret2")
        account = Account.objects.create(city=city, country=country,
                                         user=self.user)
        account.save()
        accountspar = Account.objects.create(city=city,
                                             country=country,
                                             user=self.spartan)
        accountspar.save()
        self.category = Category.objects.create(name="TestCategory",
                                                path_banner="test")
        self.category.save()
        spartan = Spartan.objects.create(last_name="Males",
                                         first_name="Sebastian",
                                         birthday="2014-03-12",
                                         address="La mine acas",
                                         cnp="dawd2",
                                         series="dawdaw",
                                         user=self.spartan,
                                         spartanStatus=True)
        spartan.save()

    def test_invalid_spartan_form(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '2013',
                     'address': 'Lestrada', 'cnp': '&&&',
                     'series': 'Dwda'}
        form = CreateSpartanForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_is_already_spartan(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '2013-02-13',
                     'address': 'Lestrada', 'cnp': '12313',
                     'series': 'Dwda',
                     'category': self.category.name}
        form = CreateSpartanForm(data=form_data)
        self.assertFalse(form.is_valid())

    def tests_user_is_not_spartan(self):
        form_data = {'last_name': 'Gheorge',
                     'first_name': 'CelFrumos', 'birthday': '02/13/2016',
                     'address': 'Lestrada', 'cnp': '1231d3',
                     'series': 'Dwda',
                     'category': self.category.name}
        form = CreateSpartanForm(data=form_data)
        self.assertFalse(form.is_valid())
