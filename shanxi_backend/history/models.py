# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.CharField(max_length=50, null=True)
    contents = models.CharField(max_length=300, null=True)
    color = models.CharField(max_length=300, null=True)