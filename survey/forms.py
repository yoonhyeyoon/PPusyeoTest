from django import forms
from django.forms import fields
from .models import Survey

class SurveyForm(forms.ModelForm):

    
    class Meta:
        model = Survey
        fields = '__all__'