from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    #DIRECIONARIO DE CONTEXTO EN EL ULTIMO PARAMETRO
    return render(request, "portfolio/portfolio.html", {
        'projects' : projects
    })