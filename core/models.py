# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "tags"

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"

    def __unicode__(self):
        return self.name


class News(models.Model):
    tags = models.ManyToManyField(Tag, db_table="news_tags", related_name='news', blank=True, null=True)
    categories = models.ManyToManyField(Category, db_table="news_categories", related_name='news', blank=True, null=True)
    user = models.ForeignKey(User)
    title = models.TextField(null=False)
    body = models.TextField(null=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news', null=True)
    video = models.TextField(null=True)
    creation_time = models.DateTimeField(editable=False)
    last_update_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = str(datetime.now())
        elif not self.id:
            self.creation_time = str(datetime.now())

        return super(News, self).save(*args, **kwargs)

    class Meta:
        db_table = "news"

    def __unicode__(self):
        return self.title


#Eventos
class Event(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=150)
    information = models.TextField()
    address = models.TextField()
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='events', null=True)
    start_time = models.DateTimeField(null=True)
    creation_time = models.DateTimeField(editable=False)
    last_update_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = str(datetime.now())
        elif not self.id:
            self.creation_time = str(datetime.now())

        return super(Event, self).save(*args, **kwargs)

    class Meta:
        db_table = "events"

    def __unicode__(self):
        return self.name


#Productos
class Classification(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='classifications', null=True)
    level = models.IntegerField(default=1)
    category_father = models.ForeignKey('self', null=True, related_name='children')
    creation_time = models.DateTimeField(editable=False)
    last_update_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = str(datetime.now())
        elif not self.id:
            self.creation_time = str(datetime.now())

        return super(Classification, self).save(*args, **kwargs)

    class Meta:
        db_table = "classifications"

    def __unicode__(self):
        return self.name


class Product(models.Model):
    classifications = models.ManyToManyField(Classification, db_table="products_classifications", related_name='products', blank=True)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='products', null=True)
    description = models.TextField()
    body = models.TextField()
    creation_time = models.DateTimeField(editable=False)
    last_update_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = str(datetime.now())
        elif not self.id:
            self.creation_time = str(datetime.now())

        return super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = "products"

    def __unicode__(self):
        return self.name