from django.contrib import admin

from .models import Profile, Course, StudySession

admin.site.register(Profile)
admin.site.register(StudySession)
admin.site.register(Course)