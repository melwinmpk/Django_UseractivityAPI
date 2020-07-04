import datetime
# from django.core import serializers
#####################################
import factory
# import factory.django
# from users.models import Userdata, ActivityPeriod
############################################

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework import generics, mixins, permissions
from users.models import Userdata, ActivityPeriod



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
    usractivity_periods = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Userdata
        fields = [
            'id',
            'real_name',
            'tz',
            'usractivity_periods'
        ]
        read_only_fields = ['usractivity_periods']

    def get_usractivity_periods(self, obj):
        data = ActivityPeriod.objects.filter(
            userid=obj.id).values('start_time','end_time')
        list_result = [{'start_time': entry['start_time'],'end_time': entry['end_time']} for entry in data.values()]
        return list_result


######################################
class UserdataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Userdata

    real_name = factory.Faker('first_name')
    tz = 'tz'
    #factory.Faker('first_name')


class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod
    # id = factory.Faker('id')
    userid = factory.SubFactory(UserdataFactory)
    # 2020-07-04 08: 19: 34.261290
    start_time = "2020-07-04 08: 19: 34.261290"
    end_time = "2020-07-04 10: 19: 34.261290"
    # start_time = factory.Faker(str(datetime.datetime.now()))
    # end_time = factory.Faker(str(datetime.datetime.now()))
######################################
