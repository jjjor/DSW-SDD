from django.db import models

class SeboDeDiscos(models.Model):
   nome = models.CharField(max_length=30)
   descricao = models.CharField(max_length=30)
   selo_fonografico = models.CharField(max_length=30)
   ano = models.IntegerField()
   pais = models.CharField(max_length=30)
   genero = models.CharField(max_length=30)
   quantidade = models.IntegerField()
