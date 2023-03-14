# -*- coding: utf-8 -*-
from logging import exception
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Message

# Create your views here.

@require_http_methods(['POST'])
def revise_content(request):
    if request.method == 'POST':
        page = request.POST.get('page')
        newContent = request.POST.get('contents')
        newColor = request.POST.get('color')
        if (page == 'division' or page == 'form' or page == "fusion"):
            Message.objects.create(page = page,contents = newContent,color = newColor)
            return HttpResponse('yes')
        else:
            return HttpResponse('no')

@require_http_methods(['POST'])
def get_message(request):
    if request.method == 'POST':
        page = request.POST.get('page')
        message = Message.objects.filter(page=page)
        if message:
            return JsonResponse({'data': list(message.values())})
        else:
            return JsonResponse({'data': 'message not found'})
    else:
        return HttpResponse('error')