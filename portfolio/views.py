from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def projects(request):
    return render(request, "portfolio/all-projects.html")

def specific_project(request, slug):
    return render(request, "portfolio/single-project.html", {
        "slug": slug
    })