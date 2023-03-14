'''
    common/models.py
    @description: 公用的models
'''

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
        db_table = 'test_user'