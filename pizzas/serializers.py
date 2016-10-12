from rest_framework import serializers

from .models import Pizza
from toppings.serializers import ToppingSerializer

class PizzaSerializer(serializers.ModelSerializer):
    topping_set = ToppingSerializer(many=True, read_only=True)

    total_cost = serializers.SerializerMethodField()
    
    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'description',            
            'topping_set',
            'base_price',
            'total_cost',
        )

    def get_total_cost(self, obj):
    	topping_prices = 0

    	for topping in obj.topping_set.all():
    		topping_prices += topping.price
    	total_price = topping_prices + obj.base_price
    	return total_price
