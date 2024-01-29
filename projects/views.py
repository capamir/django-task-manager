from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectUpdateForm, ProjectCreationForm

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

    def get(self, request, pk, *args, **kwargs):
        # Get the project by its ID or return a 404 response if not found
        project = get_object_or_404(Project, id=pk)

        # Pass the project to the template
        context = {
            'project': project
        }

        # Render the template with the context
        return render(request, self.template_name, context)

class ProjectCreateView(View):
    template_name = 'projects/project_form.html'

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm  # Replace with the actual form you create for updating projects
    template_name = 'projects/project_form.html'  # Replace with the actual template path
    success_url = reverse_lazy('projects:projects')  # Redirect to user_projects page after successful update

    def form_valid(self, form):
        # Optionally, you can add logic here for additional processing when the form is valid
        return super().form_valid(form)