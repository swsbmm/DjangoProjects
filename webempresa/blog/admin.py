from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # Esto funciona para ver los campos que no se muestran automaticamente en el admin.
    read_only_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    read_only_fields = ('created','updated')
    # Para ver las columnas en el admin
    list_display = ('title','author','published','post_categories',)
    # Para ordernar por author y luego por fecha de publicacion.
    ordering = ('author','published',)
    # Formulario de busqueda por titulo o por mas campos, para buscar por datos relacionados se tiene que usar la sintaxis del author__username
    # o por categorias  de la siguiente manera: categories__name
    search_fields = ('title','author__username','categories__name')
    # gerarquia de fechas
    date_hierarchy = 'published'
    # Campos para que los filtre, generalmente los campos de filtrado son relaciones 
    list_filter = ('categories__name', 'author__username',)
    # para agregar la columna de categorias

    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by("name"))
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)