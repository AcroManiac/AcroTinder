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

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

	# level_description
	# comfort_time

class Sport(models.Model):
	name = models.CharField(max_length=64, blank=False, default='Pair Sport')

class Level(models.Model):
	name = models.TextField(max_length=20, default='Beginner')

class Position(models.Model):
	name = models.TextField(max_length=20, default='Base')
