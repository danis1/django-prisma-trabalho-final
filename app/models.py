from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='servicos')
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="servicos/", blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    



class Produto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='produtos')
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.servico.nome