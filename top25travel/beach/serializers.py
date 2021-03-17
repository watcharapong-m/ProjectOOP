from rest_framework import serializers 
from .models import top25travel
 
 
class top25travelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = top25travel
        fields = '__all__'