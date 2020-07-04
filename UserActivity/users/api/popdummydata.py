import factory
from users.models import Userdata, ActivityPeriod
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     name = factory.Faker('name')
#     address = factory.Faker('address')
#     phone_number = factory.Faker('phone_number')

######################################


class UserdataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Userdata

    real_name = factory.Faker('first_name')
    tz = factory.Iterator(['America/Los_Angeles', 'Asia/Kolkata', 'Asia/Singapore', 'Asia/Hong Kong' ])
    #factory.Faker('first_name')


class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod
    # id = factory.Faker('id')
    userid = factory.SubFactory(UserdataFactory)
    # 2020-07-04 08: 19: 34.261290
    start_time = factory.Iterator(["2020-07-04 08: 19: 34.261290", "2020-07-04 09: 19: 34.261290", "2020-07-04 08: 30: 34.261290", "2020-07-04 08: 35: 34.261290"])
    end_time = factory.Iterator(["2020-07-04 10: 19: 34.261290", "2020-07-04 11: 19: 34.261290", "2020-07-04 12: 19: 34.261290", "2020-07-04 10: 13: 34.261290"])
    # start_time = factory.Faker(str(datetime.datetime.now()))
    # end_time = factory.Faker(str(datetime.datetime.now()))
######################################
