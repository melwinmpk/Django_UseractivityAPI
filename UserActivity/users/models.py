from django.db import models

# Create your models here.
'''
    User
    -> id (Primary)
    -> real_name (foreignkey)
    -> tz

    ActivityPeriod
    -> userid (foreign key)
    -> start_time
    -> end_time

'''

class User(models.Model):
    id   = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, null=False, default=None)
    real_name = models.CharField(max_length=100, blank=True, null=True)
    tz = models.CharField(max_length=100, blank=True, null=True)


class ActivityPeriod(models.Model):
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    start_time = models.CharField(max_length=300, blank=True, null=True)
    end_time = models.IntegerField(blank=False, null=False, default=0)
