from rest_framework.serializers import ModelSerializer
from board.models import Board
from board.models import Employee


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


class EmployeeSerializer(ModelSerializer): #list
    class Meta:
        model = Employee
        fields = ['id', 'lname', 'fname', 'email', 'hdate', 'deptid']

    def get_deptid(self, obj):
        if obj.deptid == None:
            return 0
        return obj.deptid

class EmployeeDetailSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'lname', 'fname', 'email', 'phone', 'hdate', 'jobid', 'sal', 'mgrid', 'deptid']

