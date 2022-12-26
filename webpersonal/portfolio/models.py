from django.db import models

# Create your models here.

# De esta manera se define un modelo, lo que representa una tabla en la base de datos

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo");
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")
    
    # para definir el nombre del proyecto en el admin se define la clase meta
    class Meta:
        verbose_name =  "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created']
    # Para que los proyectos tengan nombre en ves de "objects"

    def __str__(self):
        return self.title