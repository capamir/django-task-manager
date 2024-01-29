from django import forms
from .models import Project, Task

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class TaskCreateForm(forms.ModelForm):
    user_id = forms.CharField()

    class Meta:
        model = Task
        fields = ['title', 'description']