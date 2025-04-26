from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls={
        'All_items':'/all',
        'Search by category':'/?category=cateogry_name',
        'Search by subcategory':'/?subcategory=subcateogry_name',
        'Add':'create',
        'Update':'update/pk',
        'Delete':'item/pk/delete'

    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item=ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data is already exist')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def all_items(request):
    if request.query_params:
        items=Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    if items:
        serializers=ItemSerializer(items,many=True)
        return Response(serializers.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_item(request,pk):
    item=Item.objects.get(pk=pk)
    data=ItemSerializer(instance=item,data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
