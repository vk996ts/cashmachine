# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Card


class CardCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=u'PIN', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Confirm PIN', widget=forms.PasswordInput)

    class Meta:
        model = Card
        fields = ('number', 'amount')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(u"PINs not equal")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CardCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CardChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Card
        fields = ['number', 'password', 'amount', 'is_active', 'is_admin']

    def clean_password(self):
        return self.initial["password"]


class CardAdmin(UserAdmin):
    form = CardChangeForm
    add_form = CardCreationForm

    list_display = ('number', 'amount', 'is_active', 'is_admin')
    list_filter = ('is_active',)
    search_fields = ('number',)
    filter_horizontal = ()
    ordering = ('number',)

    fieldsets = (
        (None, {'fields': ('number', 'password', 'amount', 'is_active', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('number', 'amount', 'is_active', 'is_admin', 'password1', 'password2')}
        ),
    )


admin.site.register(Card, CardAdmin)

admin.site.unregister(Group)
