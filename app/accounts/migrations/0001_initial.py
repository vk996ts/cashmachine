# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('number', models.CharField(unique=True, max_length=19, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='\u0421\u0447\u0435\u0442')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u0430\u044f')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0430',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u044b',
            },
        ),
    ]
