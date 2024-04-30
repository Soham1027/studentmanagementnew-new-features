from django import forms 
from .models import timetable
from django.contrib.auth.models import User

class UserUpdate(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','email']
      
class addtt(forms.ModelForm):
     class Meta:
        model= timetable
        fields='__all__'