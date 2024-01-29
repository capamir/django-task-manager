from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Project, Task
from .forms import ProjectUpdateForm, ProjectCreationForm, TaskCreateForm
from accounts.models import User
# Create your views here.

class ProjectsView(View):
    template_name = 'projects/projects.html'

    def get(self, request, *args, **kwargs):
        # Get the projects created by the current user
        user_projects = Project.objects.filter(created_by=request.user)

        # Pass the user_projects to the template
        context = {
            'projects': user_projects
        }

        # Render the template with the context
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        project_creation_form = ProjectCreationForm(request.POST)

        if project_creation_form.is_valid():
            # Save the new project with the current user as the creator
            new_project = project_creation_form.save(commit=False)
            new_project.created_by = request.user
            new_project.save()

            return redirect('projects:projects')  # Redirect to the projects page or any other desired page upon successful project creation
        else:
            # If the form is not valid, render the template again with the form and display validation errors
            user_projects = Project.objects.filter(created_by=request.user)
            context = {
                'projects': user_projects,
                'project_creation_form': project_creation_form,
            }
            return render(request, self.template_name, context)

class ProjectDetailView(View):
    template_name = 'projects/single-project.html'
    form_class = TaskCreateForm

    def get(self, request, *args, **kwargs):
        # Get the project by its ID or return a 404 response if not found
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        # Get tasks related to the project
        project_tasks = Task.objects.filter(project=project)

        # Pass the project and the form to the template
        context = {
            'project': project,
            'tasks': project_tasks,
            'form': self.form_class(),  # Pass the project to the form
        }

        # Render the template with the context
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        form = self.form_class(request.POST)

        if form.is_valid():
            # Save the new task with the current project
            new_task = form.save(commit=False)
            new_task.project = project
            user = get_object_or_404(User, id=form.cleaned_data['user_id'])
            new_task.assigned_to = user

            new_task.save()

            return redirect('projects:project', pk=project.pk)  # Redirect to the project detail page upon successful task creation
        else:
            # If the form is not valid, render the template again with the form and display validation errors
            context = {
                'project': project,
                'form': task_creation_form,
            }
            return render(request, self.template_name, context)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm  # Replace with the actual form you create for updating projects
    template_name = 'projects/project_form.html'  # Replace with the actual template path
    success_url = reverse_lazy('projects:projects')  # Redirect to user_projects page after successful update

    def form_valid(self, form):
        # Optionally, you can add logic here for additional processing when the form is valid
        return super().form_valid(form)

class TaskDetailsView(View):
    template_name = 'projects/task-details.html'

    def get(self, request, *args, **kwargs):
        # Get the project by its ID or return a 404 response if not found
        task = get_object_or_404(Task, id=self.kwargs['pk'])

        context = {
            'task': task,
        }

        # Render the template with the context
        return render(request, self.template_name, context)

class TaskCompleteView(View):
    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=task_id)

        # Update the task's 'completed' field to True
        task.completed = True
        task.save()

        # Redirect back to the project detail page or any other desired page
        return redirect('projects:project', pk=task.project.pk)