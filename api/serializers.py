# api/serializers.py
from rest_framework import serializers
from .models import CustomUser, Employee, Device
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_employee', 'is_admin']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_employee', 'is_admin']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_employee=validated_data.get('is_employee', False),
            is_admin=validated_data.get('is_admin', False)
        )
        return user

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'full_name', 'position']

class DeviceSerializer(serializers.ModelSerializer):
    assigned_to = EmployeeSerializer(read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'serial_number', 'assigned_to', 'purchase_date']
