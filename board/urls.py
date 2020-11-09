from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('view/', views.view),
    path('write/', views.write),
    path('update/', views.update),
    path('delete/', views.delete)
]
