from rest_framework import serializers
#from django.core.exceptions import ValidationError
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name cannot contain numbers.")
            return value
