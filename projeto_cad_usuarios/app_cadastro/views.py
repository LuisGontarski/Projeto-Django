from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novoUsuario = Usuario()
    novoUsuario.Nome = request.POST.get('nome')
    novoUsuario.Idade = request.POST.get('idade')
    novoUsuario.save()

    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    return render (request, 'usuarios/usuarios.html', usuarios)
