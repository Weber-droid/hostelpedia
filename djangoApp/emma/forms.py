from .models import Students
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'message']