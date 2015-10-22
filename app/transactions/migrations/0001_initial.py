# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operation_code', models.PositiveIntegerField(default=1, verbose_name='\u041a\u043e\u0434 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438', choices=[(1, '\u0421\u043d\u044f\u0442\u0438\u0435 \u0434\u0435\u043d\u0435\u0433'), (2, '\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0431\u0430\u043b\u0430\u043d\u0441\u0430'), (3, '\u041e\u0448\u0438\u0431\u043a\u0430: \u041d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432'), (4, '\u041e\u0448\u0438\u0431\u043a\u0430: \u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043f\u0438\u043d-\u043a\u043e\u0434'), (5, '\u041e\u0448\u0438\u0431\u043a\u0430: \u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043a\u0430\u0440\u0442\u044b'), (6, '\u041a\u0430\u0440\u0442\u0430 \u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u0430')])),
                ('operation_time', models.DateTimeField(auto_now=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438')),
                ('card', models.ForeignKey(verbose_name='\u041a\u0430\u0440\u0442\u0430', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438',
            },
        ),
    ]
