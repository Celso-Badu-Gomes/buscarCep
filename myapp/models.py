from django.db import models

# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=200)
    complemento2 = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    
    def ___str___(self):
        return self.logradouro + " - " + self.bairro