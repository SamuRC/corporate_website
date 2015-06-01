# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150528_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
