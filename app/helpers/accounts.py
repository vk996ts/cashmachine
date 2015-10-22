# -*- coding: utf-8 -*-
__author__ = 'vitaliy'

import re


def match_number(number):
    number_match = re.match(r'(?P<number>[1-9]{1}[0-9]{15})', number)
    if number_match and number_match.groupdict()['number'] == number:
        return False
    return True


def match_password(password):
    password_match = re.match(r'(?P<password>[0-9]{4})', password)
    if password_match and password_match.groupdict()['password'] == password:
        return False
    return True
