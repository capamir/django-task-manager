from django.db import models
from accounts.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)