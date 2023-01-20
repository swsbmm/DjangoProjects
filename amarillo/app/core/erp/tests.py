from config.wsgi import *
from core.erp.models import Type

# Listar

print(Type.objects.all())