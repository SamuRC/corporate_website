# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
