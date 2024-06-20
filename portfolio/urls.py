from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("projects", views.projects, name="projects-page"),
    path("projects/<slug:slug>", views.specific_project, name="project-detail-page")
]