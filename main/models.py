from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.db import models


class GenderChoices(models.IntegerChoices):
    MALE = 0, 'Мужской'
    FEMALE = 1, 'Женский'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices)
    location = PointField(null=True)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()


class UserPhoto(models.Model):
    user = models.ForeignKey(UserProfile, related_name='photos', related_query_name='photo', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/')
