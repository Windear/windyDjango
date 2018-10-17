from rest_framework import serializers
from .models import Collection_net, Friends_net


class collectionNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection_net
        fields = ('id', 'icon', 'net_name', 'link_url')


class friendsNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends_net
        fields = ('id', 'net_name', 'link_url')
