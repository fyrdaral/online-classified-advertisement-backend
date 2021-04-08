from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(source='owner.id')
    owner_username = serializers.CharField(source='owner.username')
    department_name = serializers.CharField(source='department.name')

    class Meta:
        model = Advertisement
        fields = (
            'id',
            'title',
            'description',
            'department_name',
            'owner_id',
            'owner_username',
            'date_created',
            'last_modified',
            'price',
            'size',
            'state',
        )
