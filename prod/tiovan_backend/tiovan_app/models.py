from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

from django.conf import settings

class Endereco(models.Model):
    logradouro = models.CharField(max_length=120, null=True)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.logradouro

class Motorista(models.Model):
    nome = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cpf = models.CharField(max_length=15, unique=True)
    celular = models.CharField(max_length=100, null=True, blank=True, default=None)
    imagem = models.CharField(max_length=1000000, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_DEFAULT, default=None)
    def __str__(self):
        return self.nome

class Instituicoes(models.Model):
    class Meta:
        verbose_name_plural = "Instituicoes"
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=None)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=100)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=200)
    celular = models.CharField(max_length=100, null=True, blank=True, default=None)
    cpf = models.CharField(max_length=15, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_DEFAULT, default=None)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_DEFAULT, default=None, null=True)
    def __str__(self):
        return self.nome

class Dependente(models.Model):
    nome = models.CharField(max_length=200)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_DEFAULT, default=None, null=True)
    instituicao = models.ForeignKey(Instituicoes, on_delete=models.SET_DEFAULT, default=None, null=True)
    def __str__(self):
        return self.nome