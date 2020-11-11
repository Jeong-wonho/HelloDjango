from rest_framework.serializers import ModelSerializer
from board.models import Board


class BoardSerializer(ModelSerializer): #list
    class Meta:
        model = Board
        fields = ['id', 'title', 'userid', 'regdate', 'views', 'thumbup']


class BoardDetailSerializer(ModelSerializer): #Detail
    class Meta:
        model = Board
        fields = ['id', 'title', 'userid', 'regdate', 'views', 'thumbup', 'contents']


class BoardCreateSerializer(ModelSerializer): #Create
    class Meta:
        model = Board
        fields = ['title', 'userid', 'contents']
