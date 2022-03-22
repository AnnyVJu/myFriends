# coding=utf-8
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

GENDER_CHOICES = [
    ['male', "Male"],
    ['female', "Female"],
]

REL_CHOICES = [
    ['none', "None"],
    ['single', "Single"],
    ['in_a_rel', "In a relationship"],
    ['engaged', "Engaged"],
    ['married', "Married"],
    ['in_love', "In love"],
    ['complicated', "Complicated"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    avatar = models.FileField(verbose_name="Avatar", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="About me")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="City")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Birthday")
    gender = models.CharField(max_length=10, verbose_name="Gender", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name="Relationship", choices=REL_CHOICES, default="none")

    def __str__(self):
        return self.user


class Post(models.Model):
    datetime = models.DateTimeField(verbose_name=u"Дата", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Автор", related_name="posts")
    text = models.CharField(max_length=1000, verbose_name=u"Текст", null=True, blank=True)
    image = models.FileField(verbose_name=u"Картинка", null=True, blank=True)

    class Meta:
        ordering = ["-datetime"]


class Comment(models.Model):
    datetime = models.DateTimeField(verbose_name=u"Дата", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Автор", related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"Пост", related_name="comments")
    text = models.CharField(max_length=1000, verbose_name=u"Текст", null=True, blank=True)

    class Meta:
        ordering = ["datetime"]
