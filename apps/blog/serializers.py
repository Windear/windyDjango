from rest_framework import serializers
from .models import BlogArticle



class BlogsSerializer(serializers.ModelSerializer):
    picture = serializers.CharField()

    class Meta:
        model = BlogArticle
        fields = ('id', 'picture','title','tag','introduction', 'author','is_original','create_time')
