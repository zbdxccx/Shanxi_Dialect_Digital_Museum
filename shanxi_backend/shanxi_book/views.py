from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt
from .models import Book

from django.db import connection
import json

# Create your views here.
# @csrf_exempt

'''
def login_test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            return HttpResponse('login success')
        else:
            return HttpResponse('login failed')
    else:
        return
'''


@require_http_methods(['POST'])
def search_book(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        book = Book.objects.filter(name__contains=bookname, author__contains=author, publisher__contains=publisher)

        for i in book:
            print(i.id, i.name, i.author, i.publisher, i.img_path)

        if book:
            return JsonResponse({'data': list(book.values())})
        else:
            return JsonResponse({'data': 'book not found'})
    else:
        return HttpResponse('error')

@require_http_methods(['POST'])
def get_book_by_name(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        book = Book.objects.filter(name=bookname)
        if book:
            return JsonResponse({'data': list(book.values())})
        else:
            return JsonResponse({'data': 'book not found'})
    else:
        return HttpResponse('error')


@require_http_methods(['POST'])
def search_book_num(request):
    if request.method == 'POST':
        book_num = Book.objects.all().count()
        if book_num >= 0:
            return HttpResponse(str(book_num))
        else:
            return HttpResponse("暂无数据")
