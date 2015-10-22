# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from django.contrib import admin


from .models import CardOperation


class CardOperationAdmin(admin.ModelAdmin):
    list_display = ('card', '__unicode__', 'operation_time')

    list_filter = ('operation_code', 'card__number')

admin.site.register(CardOperation, CardOperationAdmin)