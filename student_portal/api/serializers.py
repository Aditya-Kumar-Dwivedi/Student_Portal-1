from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','user_name','password')

class StudentVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('user_name','password')