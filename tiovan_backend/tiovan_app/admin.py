# Register your models here.
from django.contrib import admin
from .models import Motorista, Endereco

# TokenAdmin.raw_id_fields = ['user']
admin.site.register(Motorista)
admin.site.register(Endereco)
