from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("projects", views.projects, name="projects-page"),
    path("projects/<slug:slug>", views.single_project, name="project-detail-page"),
    path("about-me", views.about_me, name="about-me")
]

handler404 = 'portfolio.views.custom_404'