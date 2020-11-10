from django.db import models
from django.utils import timezone
# Create your models here.

class Board(models.Model):
    # id = models.IntegerField() #자동생성이므로 생략 가능
    title = models.CharField(max_length=100)
    userid = models.CharField(max_length=18)
    regdate = models.DateTimeField(default=timezone.localtime)
    views = models.IntegerField(default=0)
    thumbup = models.IntegerField(default=0)
    contents = models.TextField()

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    hdate = models.DateField()
    jobid = models.CharField(max_length=20)
    sal = models.IntegerField()
    commpct = models.FloatField()
    mgrid = models.IntegerField()
    deptid = models.IntegerField()


