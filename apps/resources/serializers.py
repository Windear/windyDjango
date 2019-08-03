from rest_framework import serializers
from .models import Resources, CloudDrive


class CloudDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudDrive
        fields = '__all__'


class ResourcesSerializer(serializers.ModelSerializer):
    # cloud_drive = CloudDriveSerializer(many=True)

    class Meta:
        model = Resources
        fields = ('id', 'picture', 'title', 'file_type','cate')
