from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')    

        if senha != confirmar_senha:
            print('Erro 1')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            print('Erro 2')
            return redirect('/usuarios/cadastro')
          
        users = User.objects.filter(username=username)  
        
        if users.exists():
          return redirect('/usuarios/cadastro')        
        
        user = User.objects.create_user(
          username=username,
          email=email,
          password=senha,
        )
        
        return redirect('/usuarios/login')      