from django.contrib import admin
from .models import Perfil

admin.site.register(Perfil)


# @admin.register(Servico)
# class ServicoAdmin(admin.ModelAdmin):
#     list_display = ["nome", "descricao", "preco", "imagem", "categoria", "ativo"]
#     list_filter = ["categoria", "ativo"]
#     search_fields = ["nome", "descricao"]
#     ordering = ["nome", "preco"]
#     list_per_page = 2