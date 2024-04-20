from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')    
        
        if not username:
            messages.add_message(request, constants.ERROR, 'O campo username não pode ser vazio')
            return redirect('/usuarios/cadastro')
          
        if not email:
            messages.add_message(request, constants.ERROR, 'O campo email não pode ser vazio')
            return redirect('/usuarios/cadastro')          

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e o confirmar senha deve ser iguais')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter mais que 6 dígitos')
            return redirect('/usuarios/cadastro')
          
        users = User.objects.filter(username=username)  
        
        if users.exists():
          messages.add_message(request, constants.ERROR, 'Já existe um usuário cadastrado com esse username')
          return redirect('/usuarios/cadastro')        
        
        user = User.objects.create_user(
          username=username,
          email=email,
          password=senha,
        )
        
        return redirect('/usuarios/login')      