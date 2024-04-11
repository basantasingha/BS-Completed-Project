from django.shortcuts import render
from rest_framework import viewsets
from . models import BlogModel
from . serializers import Blogserializer
# Create your views here.
class Blogviewset(viewsets.ModelViewSet):
        queryset = BlogModel.objects.all()
        serializer_class=Blogserializer