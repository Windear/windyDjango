from rest_framework import serializers
from .models import DesignWorks


class DesignListSerializer(serializers.ModelSerializer):
    # cloud_drive = CloudDriveSerializer(many=True)

    class Meta:
        model = DesignWorks
        fields = ('id', 'title', 'dgndatetime', 'picture', 'cate', 'active',)
        # fields = '__all__'


class DesignDetailSerializer(serializers.ModelSerializer):
    # cloud_drive = CloudDriveSerializer(many=True)

    class Meta:
        model = DesignWorks
        # fields = ('id', 'title', 'dgndatetime', 'picture', 'cate', 'active',)
        fields = '__all__'
