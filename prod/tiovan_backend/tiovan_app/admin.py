# Register your models here.
from django.contrib import admin
from .models import Motorista, Endereco, Instituicoes, Responsavel, Dependente

# TokenAdmin.raw_id_fields = ['user']
admin.site.register(Motorista)
admin.site.register(Endereco)
admin.site.register(Instituicoes)
admin.site.register(Responsavel)
admin.site.register(Dependente)
