# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from django.db import models


from accounts.models import Card
from helpers.lists import get_display


OPERATION_CODES = (
    (1, u'Get Cash'),
    (2, u'Get Balance'),
    (3, u'Error: Not enough money'),
    (4, u'Error: Wrong PIN'),
    (5, u'Error: Card Blocking'),
    (6, u'Card is blocked'),
)


class CardOperation(models.Model):
    card = models.ForeignKey(Card, verbose_name=u'Card', related_name='operations')
    operation_code = models.PositiveIntegerField(default=1, choices=OPERATION_CODES, verbose_name=u'Operation code')
    operation_time = models.DateTimeField(auto_now=True, verbose_name=u'Operation Time')

    def __unicode__(self):
        return self.get_operation_code_display()

    class Meta:
        verbose_name = u'Operation'
        verbose_name_plural = u'Operations'