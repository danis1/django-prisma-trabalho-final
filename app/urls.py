from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("servicos", views.servicos, name="servicos"),
    
    path("produtos", views.produtos, name="produtos"),
    
    path("add-servico", views.addServico, name="addServico"),
    
    path("del-servico/<int:id_servico>", views.delServico, name="delServico"),
    
    path("edit-servico/<int:id_servico>", views.editServico, name="editServico"),
    
    path("integrantes", views.integrantes, name="integrantes"),
    
    path("add-integrante", views.addIntegrante, name="addIntegrante"),
    
    path("del-integrante/<int:id_integrante>", views.delIntegrante, name="delIntegrante"),
    
    path('categoria-api/', views.categoriasAPI, name='categoriasAPI'),
    path('categoria-api/<int:id_categoria>', views.categoriaAPI, name="categoriaAPI"),    
   
    path('relatorios', views.relatorios, name='relatorios'), 

    path("comprar/<int:id_servico>", views.comprar, name="comprar"),

    path("carrinho", views.carrinho, name="carrinho"),

    path("edit-integrante/<int:id_integrante>", views.editIntegrante, name="editIntegrante"),

   path("quem-somos", views.quemSomos, name="quemSomos"),
]