from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('reviseContent/', views.revise_content),
    path('getMessage/',views.get_message)
]