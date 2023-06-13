from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    #usuario.com
    path("",views.home,name = "home"),
    #usuario.com/usuarios
    path("usuario/", views.usuario, name="listagemUsuarios")

]
