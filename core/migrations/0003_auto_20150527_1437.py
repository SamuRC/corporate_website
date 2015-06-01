# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150526_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='categories',
            field=models.ManyToManyField(related_name=b'news', null=True, to=b'core.Category', db_table=b'news_categories', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(related_name=b'news', null=True, to=b'core.Tag', db_table=b'news_tags', blank=True),
        ),
    ]
