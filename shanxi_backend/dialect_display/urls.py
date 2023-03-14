from django.urls import path
from . import views

urlpatterns = [
   path("get_dialect_search_result/", views.get_dialect_search_result),
    path("get_dialect_advanced_search_result/", views.get_dialect_advanced_search_result),
    path("get_dialect_by_id/", views.get_dialect_by_id),
    path("get_classification_search_result/", views.get_classification_search_result),
    path("get_classification_by_name/", views.get_classification_by_name),
    path("get_common_classification/", views.get_common_classification),
]
