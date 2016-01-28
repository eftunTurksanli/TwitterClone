from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(null=True, blank=True)


class Tweet(models.Model):
    owner = models.ForeignKey(User)
    date = models.DateTimeField(blank=False, auto_now=False, auto_now_add=True)
    context = models.CharField(max_length=140)
    image = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, symmetrical=False, related_name='like')
    ordering = ['-date']


class Following(models.Model):
    following = models.ForeignKey(User, related_name='following', null=True)
    follower = models.ForeignKey(User, related_name='follower', null=True)
    date = models.DateTimeField(blank=True, auto_now=False, auto_now_add=True)


class Messages(models.Model):
    send_from = models.ForeignKey(User, related_name='send_from')
    send_to = models.ForeignKey(User, related_name='send_to')
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(blank=False, auto_now=False, auto_now_add=True)
    read = models.BooleanField(default=False)
