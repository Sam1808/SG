"""spider_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from spider_market.views import RegistrationApiView, CategoriesView, CompaniesView, ProductView, ActiveProductsView, CreateProductView, ModifyProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('registr/', RegistrationApiView.as_view(), name='registr'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('activeproducts/', ActiveProductsView.as_view(), name='activeproducts'),
    path('createproduct/', CreateProductView.as_view(), name='createproduct'),
    path('modifyproduct/<int:pk>', ModifyProductView.as_view(), name='modifyproduct'),
]
