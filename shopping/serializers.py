from rest_framework import serializers
from shopping.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='id', many=True)

    class Meta:
        model = Product
        fields = ('name', 'categories', 'description', 'price', 'sales_number', 'inventory_number')
