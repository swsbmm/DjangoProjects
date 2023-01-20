from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['-id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['-id']

class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=15, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateField(auto_now=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank=True)
    avatar = models.FileField(upload_to='hojaVida/%y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        db_table='empleado'
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        ordering = ['-id']
