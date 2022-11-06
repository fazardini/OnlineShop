from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.BigIntegerField()
    sales_number = models.IntegerField()
    inventory_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
