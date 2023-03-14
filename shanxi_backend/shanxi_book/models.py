from django.db import models


# Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     class Meta:
#         db_table = 'test_user'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255)
    content = models.TextField(max_length=511, null=True)

    class Meta:
        db_table = 'book'
