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

from django import forms

from .models import Review


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['message']

    def clean_message(self):
        message = self.cleaned_data['message']
        if(
                message.isdigit() or message == '' or
                not message.isalnum or not message.isalpha
        ):
            raise forms.ValidationError("Enter a valid review message")
        return message
