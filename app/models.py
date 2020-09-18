# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# from simple_history.models import HistoricalRecords # Tracking changes


# Create your models here.
class PERSON(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    in_out = models.BooleanField()
    # history = HistoricalRecords()

    def __str__(self):
        return "{} a person is comming: {}".format(self.time, self.in_out)
    class Meta:
        db_table = 'PERSON'
    #   verbose_name = ''
        ordering = ['-time', 'in_out']
        get_latest_by = 'time'
        # unique_together = (('time',))


class FACE(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField()
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(7)])
    # history = HistoricalRecords()

    def __str__(self):
        return "{} a Male:{}, age:{} is comming".format(
            self.time,
            self.gender,
            self.age)

    class Meta:
        db_table = 'FACE'
        ordering = ['-time']
        # unique_together = (('time'),)


class Time_opt(models.Model):
    TIME_CHOICES = (
        ('9',  '09:00 - 10:00'),
        ('10', '10:00 - 11:00'),
        ('11', '11:00 - 12:00'),
        ('12', '12:00 - 13:00'),
        ('13', '13:00 - 14:00'),
        ('14', '14:00 - 15:00'),
        ('15', '15:00 - 16:00'),
        ('16', '16:00 - 17:00'),
        ('17', '17:00 - 18:00'),
        ('18', '18:00 - 19:00'),
        ('19', '19:00 - 20:00'),
    )
    date = models.CharField(max_length=100)  
    hour = models.CharField(max_length=100, choices=TIME_CHOICES) 
    

    
class ericapp_peoplemove(models.Model):
    ps = models.CharField(max_length=200) 
    getin = models.CharField(max_length=200) 
    date_created = models.DateTimeField(auto_now_add=True) 
    out = models.CharField(max_length=200) 

    def __str__(self):
        return "{}, people enter : {}, people depart : {}.".format(self.date_created, self.getin, self.out)

    class Meta:
        db_table = 'ericapp_peoplemove'


class ericapp_agender(models.Model):
    ps = models.CharField(max_length=200) 
    date_created = models.DateTimeField(auto_now_add=True)
    age = models.CharField(max_length=200) 
    gender = models.CharField(max_length=200) 


    # history = HistoricalRecords()

    def __str__(self):
        return "{}, Gender : {}, Age : {} is comming".format(
            self.date_created,
            self.gender,
            self.age)
    class Meta:
        db_table = 'ericapp_agender'