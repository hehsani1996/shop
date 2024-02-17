from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 11, decimal_places = 2)
    datetime_created = models.DateTimeField(auto_now_add = True)
    datetime_modefide = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class Comment(models.Model):
    stars = [('1','very bad'),('2','bad'),('3','normal'),('4','good'),('5','very good')]
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name ='comments' )
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name ='comments' )
    body = models.TextField()
    point = models.CharField(max_length = 12, choices = stars)
    datetime_created = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)