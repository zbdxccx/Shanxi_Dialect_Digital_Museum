"""shanxi_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from test import urls as test_urls
from history import urls as history_urls
from shanxi_book import urls as book_urls
from product import urls as product_urls
from dialect_display import urls as dialect_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include(test_urls)),
    path('history/', include(history_urls)),
    path('shanxi_book/', include(book_urls)),
    path('product/',include(product_urls)),
    path('dialect_display/',include(dialect_urls))
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
