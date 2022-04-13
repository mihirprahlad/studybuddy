from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=300)
    major = models.CharField(max_length=50)
    courses = models.ManyToManyField('Course', blank=True)

class StudySession(models.Model):
    users = models.ManyToManyField(User)
    #time = models.CharField(max_length=10, default='')
    #date = models.CharField(max_length=10, default='')
    location = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=10, default='')
    #summary = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=100,default='')
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)

class Course(models.Model):
    courseAbbv = models.CharField(max_length=5, default='')
    courseNumber = models.CharField(max_length=5, default='')
    courseTitle = models.CharField(max_length=120, null=True, default='')
    courseTopic = models.CharField(max_length=120, null=True, default='')

    def __str__(self):
        return self.courseAbbv

# class Event(models.Model):
#     date = models.DateField()
#     partners = models.ManyToManyField('User', blank=True)

