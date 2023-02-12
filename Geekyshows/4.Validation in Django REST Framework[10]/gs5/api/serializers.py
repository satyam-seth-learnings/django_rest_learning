from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.Serializer):
    # name=serializers.CharField(max_length=100)
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        print(instance.name)
        instance.name=validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='rohit' and ct.lower()!='ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data