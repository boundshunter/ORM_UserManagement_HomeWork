from django.db import models

# Create your models here.


class GroupInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=64)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)


class UserInfo(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    gender = models.IntegerField(choices=[(0, '男'), (1, '女')], default=0)
    age = models.IntegerField()
    job = models.CharField(max_length=64)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
