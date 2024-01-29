from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Project

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

class ProjectDetailView(View):
    template_name = 'projects/single-project.html'  # Replace with the actual template path

    def get(self, request, pk, *args, **kwargs):
        # Get the project by its ID or return a 404 response if not found
        project = get_object_or_404(Project, id=pk)

        # Pass the project to the template
        context = {
            'project': project
        }

        # Render the template with the context
        return render(request, self.template_name, context)