from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update-project')
]
