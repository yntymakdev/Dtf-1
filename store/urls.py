from django.contrib import admin
from django.urls import path,include

from mysite.store.views import ProductViewList

urlpatterns = [
    path('',ProductViewList(), name='product_list'),
]
