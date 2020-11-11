from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.BoardListView.as_view()),
    path('boards/create/', views.BoardCreateView.as_view()),
    path('boards/<pk>/', views.BoardDetailView.as_view()),
    path('employees/', views.EmployeeListView.as_view())

]
