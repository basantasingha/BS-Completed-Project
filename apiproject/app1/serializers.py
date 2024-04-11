from rest_framework import serializers
from . models import BlogModel

# Create serializers here.
class Blogserializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = BlogModel
                fields = 'title','content','created_at','upload_at'