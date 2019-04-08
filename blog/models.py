from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    code_material = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    balance = models.IntegerField()

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    balance = models.IntegerField()
    code =  models.IntegerField()
    img = models.CharField(max_length=900)


class Technology_map(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    date_start =  models.DateTimeField()
    date_end = models.DateTimeField()


class Technology_map_position(models.Model):
    id = models.AutoField(primary_key=True)
    technology_map_id = models.IntegerField()
    material_id = models.IntegerField()
    amount = models.IntegerField()