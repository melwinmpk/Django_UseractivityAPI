from django.db import models

# Create your models here.
'''
    User
    -> id (Primary)
    -> real_name 
    -> tz

    ActivityPeriod
    -> userid (foreign key)
    -> start_time
    -> end_time

'''

class Userdata(models.Model):
    id   = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, null=False, default=None)
    real_name = models.CharField(max_length=100, blank=True, null=True)
    tz = models.CharField(max_length=100, blank=True, null=True)


class ActivityPeriod(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, null=False, default=None)
    userid = models.ForeignKey(
        Userdata, on_delete=models.CASCADE, default=None)
    start_time = models.CharField(max_length=300, blank=True, null=True)
    end_time = models.CharField(max_length=300, blank=True, null=True)
