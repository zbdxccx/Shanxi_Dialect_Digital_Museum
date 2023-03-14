from django.urls import path
from . import views

urlpatterns = [
   path('getProduct/', views.get_product),
   path('getCollections/', views.get_collections),
   path('collect/', views.collect),
   path('deleteCollection/', views.delete_collection)
]


