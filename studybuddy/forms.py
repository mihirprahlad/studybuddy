from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'major']

class SessionForm(ModelForm):
    class Meta:
        model = StudySession
        fields = ['users', 'date', 'time', 'location', 'subject','summary','description', 'startTime', 'endTime']

# class EventForm(ModelForm):
#      class Meta:
#         model = Event
#         fields = ['event', 'date', 'organizer', 'location', ]
