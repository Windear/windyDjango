from rest_framework import serializers
from .models import Tools,HistoryVersion

class HistoryVersionSerializer(serializers.ModelSerializer):
    # cloud_drive = CloudDriveSerializer(many=True)

    class Meta:
        model = HistoryVersion
        fields = '__all__'

class ToolsSerializer(serializers.ModelSerializer):
    tools_sys = HistoryVersionSerializer(many=True)
    icon = serializers.CharField()
    #cate_type = serializers.ChoiceField(choices=Tools.CATEGORY_TYPE)
    class Meta:
        model = Tools
        fields = ('id', 'icon','title','tag', 'introduction', 'cate','tools_sys',)
