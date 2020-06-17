from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

from django.conf import settings
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=20, null=True)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)
    latitude = models.CharField(max_length=30, null=True)
    longitude = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.nome_endereco

class Motorista(models.Model):
    nome = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cpf = models.CharField(max_length=15, unique=True)
    imagem = models.ImageField(upload_to='images/', null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.nome