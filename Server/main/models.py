from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

	phone = models.CharField(max_length=30, blank=True, default=None)
	birth_date = models.DateField(null=True, blank=True, default=None)
	height = models.FloatField(null=True, blank=True, default=None)
	weight = models.FloatField(null=True, blank=True, default=None)
	bio = models.CharField(max_length=500, blank=True, default=None)

	# gender
	# level
	# level_description
	# position (role)
	# comfort_time

class Sport(models.Model):
	name = models.CharField(max_length=64, blank=False, default='Pair Sport')
