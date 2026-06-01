from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_name(self, value):
        clean_name = value.strip()
        if len(clean_name) < 2:
            raise serializers.ValidationError("Employee name must be at least 2 characters long.")
        return clean_name