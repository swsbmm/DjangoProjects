from django.shortcuts import render, HttpResponse


html_template = """"
<h1>Welcome</h1>
<ul>
    <li><a href="/">inicio</a></li>
    <li><a href="/portafolio">portafolio</a></li>
    <li><a href="/acerca-de-mi">Acerca de mi</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
"""
# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def contact (request):
    return render(request, "core/contact.html")