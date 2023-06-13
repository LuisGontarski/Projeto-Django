from django.db import models

class Usuario(models.Model):
    ID_Usuario = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=155)
    Idade = models.IntegerField()
