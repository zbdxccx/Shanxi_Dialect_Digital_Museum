# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Message

# Register your models here.
admin.site.site_header = '山西方言博物馆后台管理系统'
admin.site.index_title = '首页'
admin.site.register(Message)
