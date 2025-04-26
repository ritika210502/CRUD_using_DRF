from rest_framework import serializers
from django.db.models import fields
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id','category','subcategory','name','amount')