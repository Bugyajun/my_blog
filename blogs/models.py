# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from blogs import views
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class airticle(models.Model):
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    image = models.BinaryField(blank=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    details = models.TextField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #p = reverse('blogs:detail',kwargs={'pk':self.pk})
        return reverse('blogs:detail',kwargs={'pk':self.pk})




