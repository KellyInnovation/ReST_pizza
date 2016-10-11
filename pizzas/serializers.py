from rest_framework import serializers

from .models import Pizza
from toppings.serializers import ToppingSerializer

class PizzaSerializer(serializers.ModelSerializer):
    topping_set = ToppingSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'description',            
            'topping_set',
        )