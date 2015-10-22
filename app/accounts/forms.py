# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from django import forms


from helpers.accounts import match_number, match_password


from .models import Card


class CardLoginForm(forms.Form):
    number = forms.CharField(max_length=16, required=False, widget=forms.HiddenInput, label=u'Card Number')

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('number'):
            if match_number(cleaned_data.get('number')):
                raise forms.ValidationError(u'Wrong Card Number! Should be 14 digits not starting from 0')
            try:
                card = Card.objects.get(number=cleaned_data.get('number'))
            except Card.DoesNotExist:
                raise forms.ValidationError(u'Card doesn\'t exist!')
        else:
            raise forms.ValidationError(u'Enter Card Number')
        return cleaned_data


class PinForm(forms.Form):
    number = forms.CharField(max_length=4, required=False, widget=forms.HiddenInput, label=u'PIN')

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('number'):
            if match_password(cleaned_data.get('number')):
                raise forms.ValidationError(u'Wrong PIN. Should be 4 digits.')

        else:
            raise forms.ValidationError(u'PIN is empty. Enter correct PIN')
        return cleaned_data


class CashForm(forms.Form):
    number = forms.CharField(max_length=5, required=False, widget=forms.HiddenInput, label=u'Amount')

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('number'):
            raise forms.ValidationError(u'Enter Amount.')
        return cleaned_data