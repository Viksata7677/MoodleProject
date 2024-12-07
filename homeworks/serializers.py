from rest_framework import serializers
from accounts.models import Student, CustomUser
from homeworks.models import Homework


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ['user']


class HomeworkSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Homework
        fields = '__all__'
