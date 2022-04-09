from rest_framework import serializers
from .models import Grocery


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ('name', 'nowHave', 'eaten', 'unitMeasure',
                  'min', 'purchased', 'imageURL')
