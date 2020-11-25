from rest_framework import serializers
from .models import Pizza

class Pizza_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'