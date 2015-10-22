# -*- coding: utf-8 -*-
__author__ = 'vitaliy'

import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


from helpers.accounts import match_number, match_password


class CardManager(BaseUserManager):
    """
    Manager for Card model.
    """

    def create_user(self, number, password, is_active=True, is_admin=False):

        # Creates Card and Card Account

        if match_number(number):
            raise ValueError(u"Wrong Card Number! Must be 16 digits starting from 1.")
        if match_password(password):
            raise ValueError(u"Wrong Password! Must be 4 digits.")

        card = self.model(
            number=number,
            is_active=is_active,
            is_admin=is_admin
        )

        card.set_password(password)
        card.save(using=self._db)

        return card

    def create_superuser(self, number, password):

        #creates "admin" Card

        card = self.create_user(
            number=number,
            password=password,
            is_admin=True
        )

        card.save(using=self._db)
        return card


class Card(AbstractBaseUser):
    number = models.CharField(max_length=19, unique=True, verbose_name=u'Number')
    amount = models.PositiveIntegerField(default=0, verbose_name=u'Amount')
    is_active = models.BooleanField(default=True, verbose_name=u'Is Active')
    is_admin = models.BooleanField(default=False, verbose_name=u'Is Admin')
    objects = CardManager()

    USERNAME_FIELD = 'number'

    def get_full_name(self):
        return self.number

    def get_short_name(self):
        return self.number

    def __unicode__(self):
        return self.number

    def has_perm(self, perm, obj=None):
        # Card has all permissions
        return True

    def has_module_perms(self, app_label):
        # Card has all module permissions
        return True

    @property
    def is_staff(self):
        # All admins are staff
        return self.is_admin

    def access(self, is_active=True):
        self.is_active=is_active
        self.save()

    def create_operation(self, operation_code):
        self.operations.create(operation_code=operation_code).save()

    class Meta:
        verbose_name = u'Card'
        verbose_name_plural = u'Cards'