from django.db import models
import time
import uuid


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=36, null=True)
    last_login_time = models.BigIntegerField(null=True)
    creation_time = models.BigIntegerField(editable=False)
    last_update_time = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = int(time.time())
        elif not self.id:
            self.creation_time = int(time.time())
            self.token = str(uuid.uuid4())
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = "users"

    def __unicode__(self):
        return self.person.first_name + ' ' + self.person.last_name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "tags"


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"


class News(models.Model):
    tags = models.ManyToManyField(Tag, db_table="news_tags", related_name='news', blank=True)
    categories = models.ManyToManyField(Category, db_table="news_categories", related_name='news', blank=True)
    author = models.ForeignKey(User, null=False)
    title = models.TextField(null=False)
    body = models.TextField(null=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news', null=True)
    video = models.TextField(null=True)
    creation_time = models.BigIntegerField(editable=False)
    last_update_time = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = int(time.time())
        elif not self.id:
            self.creation_time = int(time.time())

        return super(Notice, self).save(*args, **kwargs)

    class Meta:
        db_table = "news"


#Eventos
class Event(models.Model):
    tags = models.ManyToManyField(Tag, db_table="events_tags", related_name='events', blank=True)
    author = models.ForeignKey(User, null=False)
    name = models.CharField(max_length=100)
    information = models.TextField()
    address = models.TextField()
    is_published = models.BooleanField(default=True)
    start_time = models.BigIntegerField(editable=False)
    creation_time = models.BigIntegerField(editable=False)
    last_update_time = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = int(time.time())
        elif not self.id:
            self.creation_time = int(time.time())

        return super(Event, self).save(*args, **kwargs)

    class Meta:
        db_table = "events"


#Productos
class Classification(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='classifications', null=True)
    level = models.IntegerField()
    category_father = models.ForeignKey('self', null=True, related_name='children')
    creation_time = models.BigIntegerField(editable=False)
    last_update_time = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = int(time.time())
        elif not self.id:
            self.creation_time = int(time.time())

        return super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = "classifications"


class Product(models.Model):
    classifications = models.ManyToManyField(Classification, db_table="products_classifications", related_name='products', blank=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='products', null=True)
    description = models.CharField(max_length=150)
    body = models.TextField()
    creation_time = models.BigIntegerField(editable=False)
    last_update_time = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self.id:
            self.last_update_time = int(time.time())
        elif not self.id:
            self.creation_time = int(time.time())

        return super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = "products"