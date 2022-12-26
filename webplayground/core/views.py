from django.shortcuts import render
from django.views.generic.base import TemplateView


# Vista basada en clase. Hereda de un Template o clase que contiene alguna funcionalidad. en este caso TemplateView
class HomePageView(TemplateView):

    # Se define el template que esta asociado a la vista.
    template_name = "core/home.html"

    # Este metodo es propio de la clase y funciona para inyectar en el contexto nuestras propias etiquetas.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "HOLA MUNDO DE NUEVO"
        return context

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'title' : 'COSAS DEL BAJO MUNDO'
        })
