from rest_framework.serializers import HyperlinkedIdentityField,ModelSerializer,SerializerMethodField
from accounts.api.serializers import UserDetailSerializer
from firm.models import Employees


class EmployeeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'user',
            'department',
            'employee_no',
            'mobile',
            'country',
            'state',
            'city',
            'pincode',
            'salary',
        ]


class EmployeeDetailSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'user',
            'department',
            'employee_no',
            'mobile',
            'country',
            'state',
            'city',
            'pincode',
            'salary',
        ]


class EmployeeListSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'user',
            'department',
            'employee_no',
            'mobile',
            'country',
            'state',
            'city',
            'pincode',
            'salary',
        ]