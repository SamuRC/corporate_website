# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'classifications')),
                ('level', models.IntegerField()),
                ('creation_time', models.DateTimeField(editable=False)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('category_father', models.ForeignKey(related_name=b'children', to='core.Classification', null=True)),
            ],
            options={
                'db_table': 'classifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('address', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('creation_time', models.DateTimeField(editable=False)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to=b'news')),
                ('video', models.TextField(null=True)),
                ('creation_time', models.DateTimeField(editable=False)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('categories', models.ManyToManyField(related_name=b'news', db_table=b'news_categories', to='core.Category', blank=True)),
            ],
            options={
                'db_table': 'news',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(null=True, upload_to=b'products')),
                ('description', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('creation_time', models.DateTimeField(editable=False)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('classifications', models.ManyToManyField(related_name=b'products', db_table=b'products_classifications', to='core.Classification', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(related_name=b'news', db_table=b'news_tags', to='core.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
