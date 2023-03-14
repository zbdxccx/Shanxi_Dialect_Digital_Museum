from django.db import models

# Create your models here.

class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'classification'

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
    remark = models.TextField(blank=True, null=True)
    audio_path = models.CharField(max_length=255)
    classification_id = models.ForeignKey(Classification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'audio'
