from rest_framework import serializers
from .models import Student,Course

class StudentAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    