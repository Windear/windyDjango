from rest_framework import serializers
from .models import DesignWorks

class DesginListSerializer(serializers.ModelSerializer):
    # cloud_drive = CloudDriveSerializer(many=True)

    class Meta:
        model = DesignWorks
        fields = '__all__'

