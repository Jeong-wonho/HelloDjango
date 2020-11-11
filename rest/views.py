from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from board.models import Board, Employee
from rest.serializers import BoardSerializer, BoardDetailSerializer, BoardCreateSerializer, EmployeeSerializer, EmployeeDetailSerializer


class BoardListView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# class BoardDetailView(RetrieveAPIView):
class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer


class BoardCreateView(CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
