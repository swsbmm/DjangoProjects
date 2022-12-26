from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        # Rellenar el formulario con la informacion de la pagina.
        contact_form = ContactForm(data=request.POST)
        # Verficicar el formulario.
        if contact_form.is_valid():
            # recuperando datos.
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            # ENVIAMOS EL CORREO Y REDIRECCIONAMOS
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}> \n\n Escribio: \n\n {}".format(name,email,message),
                "no-contestar@inbox.mailtrap.io",
                ["swsbmm@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # ALGO NO HA IDO BIEN REDIRECCIONAMOS AL FAIL
                return redirect(reverse('contact')+"?fail")    
            

    return render(request, 'contact/contact.html',{
        'contactForm' : contact_form,
    })