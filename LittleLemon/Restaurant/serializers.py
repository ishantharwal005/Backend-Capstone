from rest_framework import serializers
from Restaurant.models import *

class bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class menuserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'