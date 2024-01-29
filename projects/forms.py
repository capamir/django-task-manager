from django import forms
from .models import Project

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']