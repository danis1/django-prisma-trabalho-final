from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Perfil(models.Model):

    TIPOS_USUARIO = [
        ('administrador', 'administrador'),
        ('cliente', 'Cliente'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='cliente')


    def __str__(self):
        return f'{self.usuario.username} - {self.tipo_usuario}'



# class Categoria(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField(blank=True)
#     ativo = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.nome

# class Servico(models.Model):
#     categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='servicos')
#     nome = models.CharField(max_length=150)
#     descricao = models.TextField(blank=True)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     imagem = models.ImageField(upload_to="servicos/", blank=True, null=True)
#     ativo = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.nome