"""
URL configuration for belousov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('add-product', views.add_product, name='add-product'),
    path('<int:pk>/update', views.UpdateProduct.as_view(), name='update-product'),
    path('<int:pk>', views.DetailProduct.as_view(), name='detail-product'),
    path('<int:pk>/delete', views.DeleteProduct.as_view(), name='delete-product'),

]
