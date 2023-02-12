from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=['name','roll','city']
        # fields=['id','name','roll','city']
        # fields='__all__'
        exclude=['roll']