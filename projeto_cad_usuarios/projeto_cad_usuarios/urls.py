from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    #usuarios.com
    path("",views.home,name = "home"),

]
