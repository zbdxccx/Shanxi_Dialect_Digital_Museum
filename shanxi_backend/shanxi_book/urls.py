from django.urls import path
from . import views

urlpatterns = [
   path("search_book/", views.search_book),
   path('search_book_num/', views.search_book_num),
   path("get_book_by_name/", views.get_book_by_name),
]
