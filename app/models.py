# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class PERSON(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    in_out = models.BooleanField()


class FACE(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField()
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(7)])
