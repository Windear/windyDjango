from rest_framework import serializers
#from .models import Resources, CATEGORY_TYPE


class ResourcesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    #cate = serializers.IntegerField(choices=CATEGORY_TYPE)
