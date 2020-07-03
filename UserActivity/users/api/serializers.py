import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework import generics, mixins, permissions
from users.models import Userdata, ActivityPeriod
# from django.core import serializers

'''
    User
    -> id (Primary)
    -> real_name 
    -> tz
'''    


class UsrActivitySerializer(serializers.ModelSerializer,
                            generics.ListAPIView):
    class Meta:
        model = ActivityPeriod
        fields = [
            'id',
            'userid',
            'start_time',
            'end_time'
        ]
        read_only_fields = ['userid']


class UserSerializer(serializers.ModelSerializer,
                     generics.ListAPIView):
    useractivity = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Userdata
        fields = [
            'id',
            'real_name',
            'tz',
            'useractivity'
        ]
        read_only_fields = ['useractivity']

    def get_useractivity(self, obj):
        data = ActivityPeriod.objects.filter(
            userid=obj.id).values('start_time','end_time')
        list_result = [entry for entry in data.values()]
        return list_result
