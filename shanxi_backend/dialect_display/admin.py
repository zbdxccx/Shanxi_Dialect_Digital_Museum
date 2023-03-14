from django.contrib import admin

# Register your models here.
from .models import Audio, Classification

# Register your models here.
admin.site.register(Audio)
admin.site.register(Classification)