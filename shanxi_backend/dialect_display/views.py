from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.decorators.csrf import csrf_exempt
from .models import Classification, Audio

from django.db import connection
import json

# Create your views here.
# @csrf_exempt

def _get_paged_result(queryset, page, page_size):
    paginator = Paginator(queryset, page_size)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return result


@require_http_methods(['POST'])
def get_dialect_search_result(request):
    if request.method == 'POST':
        search_content = request.POST.get('search_content')
        page = request.POST.get('page')
        page_size = request.POST.get('page_size')
        # 筛选Audio中name或meaning中包含search_content的数据
        audio_list = Audio.objects.filter(name__contains=search_content) | Audio.objects.filter(meaning__contains=search_content)
        total = audio_list.count()
        audio_list = _get_paged_result(audio_list, page, page_size)
        result = []
        if audio_list:
            for audio in audio_list:
                result.append({
                    'id': audio.id,
                    'name': audio.name,
                    'meaning': audio.meaning,
                    'audio_path': audio.audio_path,
                    'classification': audio.classification_id.name
                })
        return_data = {
            'length': total,
            'data': result
        }
        return JsonResponse(return_data)
    else:
        return HttpResponse('请求方式错误')

@require_http_methods(['POST'])
def get_dialect_advanced_search_result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        meaning = request.POST.get('meaning')
        classification = request.POST.get('classification')
        page = request.POST.get('page')
        page_size = request.POST.get('page_size')
        # 筛选Audio中name且meaning且classification_id.name中包含search_content的数据
        audio_list = Audio.objects.filter(name__contains=name, meaning__contains=meaning, classification_id__name__contains=classification)
        total = audio_list.count()
        audio_list = _get_paged_result(audio_list, page, page_size)
        result = []
        if audio_list:
            for audio in audio_list:
                result.append({
                    'id': audio.id,
                    'name': audio.name,
                    'meaning': audio.meaning,
                    'audio_path': audio.audio_path,
                    'classification:': audio.classification_id.name
                })
        return_data = {
            'length': total,
            'data': result
        }
        return JsonResponse(return_data)
    else:
        return HttpResponse('请求方式错误')

@require_http_methods(['POST'])
def get_dialect_by_id(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            audio = Audio.objects.get(id=id)
            return_data = {
                'id': audio.id,
                'name': audio.name,
                'meaning': audio.meaning,
                'audio_path': audio.audio_path,
                'classification': audio.classification_id.name
            }
            return JsonResponse(return_data)
        except:
            return HttpResponse(None)
    else:
        return HttpResponse('请求方式错误')

@require_http_methods(['POST'])
def get_classification_search_result(request):
    if request.method == 'POST':
        search_content = request.POST.get('search_content')
        page = request.POST.get('page')
        page_size = request.POST.get('page_size')
        # 筛选Classification中name中包含search_content的数据
        classification_list = Classification.objects.filter(name__contains=search_content)
        total = classification_list.count()
        classification_list = _get_paged_result(classification_list, page, page_size)
        result = []
        if classification_list:
            for classification in classification_list:
                result.append({
                    'id': classification.id,
                    'name': classification.name,
                    'description': classification.description
                })
        return_data = {
            'length': total,
            'data': result
        }
        return JsonResponse(return_data)
    else:
        return HttpResponse('请求方式错误')

@require_http_methods(['POST'])
def get_classification_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            classification = Classification.objects.get(name=name)
            return_data = {
                'id': classification.id,
                'name': classification.name,
                'description': classification.description
            }
            return JsonResponse(return_data)
        except:
            return HttpResponse(None)
    else:
        return HttpResponse('请求方式错误')

@require_http_methods(['POST'])
def get_common_classification(request):
    if request.method == 'POST':
        try:
            return_num = int(request.POST.get('max_num'))
        except:
            return_num = 5
            # 取出包含最多音频的前五个分类
        classification_list = Classification.objects.raw('SELECT * FROM classification ORDER BY (SELECT COUNT(*) FROM audio WHERE classification.id = audio.classification_id_id) DESC LIMIT %s', [return_num])
        result = []
        if classification_list:
            for classification in classification_list:
                result.append({
                    'id': classification.id,
                    'name': classification.name,
                    'description': classification.description
                })
        return_data = {
            'length': len(result),
            'data': result
        }
        return JsonResponse(return_data)
    else:
        return HttpResponse('请求方式错误')
