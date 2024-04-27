# Healing

O Healing e um sistema Web de tele atendimento medico, onde os médicos poderão de se cadastrar assim como o pacientes, e os médicos poderão realizar o atendimento, abrir seus horários para atendimento, visualizar o dashboards

## Design

O **Healing** e um sistema de tele medicina que, no qual foi criado de acordo com a estrutura do design, que poder ser visualizando no <a href="https://www.figma.com/file/g7xzaMum3AWGnP1B52tRLR/Healing?type=design&node-id=0%3A1&mode=dev&t=2ChGg41zQRcFMVDT-1" target="_blank">Figma</a>

## Pre-requisitos

* Necessário ter o <a href="https://www.python.org/" target="_blank">Python</a>
* Com o framework do <a href="https://www.djangoproject.com/" target="_blank">Django</a>

## Configurações iniciais

1. Primeiro devemos criar o ambiente virtual:

```bash
# Linux
python3 -m venv venv

# Windows
python -m venv venv  
```

2. Após a criação do venv vamos ativa-lo:

```bash
# Linux
source venv/bin/activate

# Windows
venv\Scripts\Activate
```

> Se o comando `venv\Scripts\Activate` não funcionar no Windows, usar o comando `.\venv\Scripts\activate`
> Caso algum comando retorne um erro de permissão execute o código e tente novamente:

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3. Agora vamos fazer a instalação do Django e as demais bibliotecas:

```bash
# Instalar o Django
pip install django

# Instalar o Pillow
pip install pillow
```

4. Vamos criar o nosso projeto Django:,

```bash
django-admin startproject healing .
```

> No comando acima, utilizando `.` faz com que a criação ocorra dentro da pasta raiz do projeto, ela e o Core do projeto
> Onde irá ter as configurações gerais do projeto

5. Rode o servidor para testar:

```bash
python manage.py runserver
```

### Configuração do Timezones

No core do projeto, no arquivo `settings.py`, alterar colocar a seguinte configuração:

```python
LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'
```

## Inicialização do server

No terminal na lina de comando executar o código:

```bash
python .\manage.py runserver
```
No qual irá inicializar o servidor do Django do server

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 20, 2024 - 13:11:49
Django version 5.0.4, using settings 'healing.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[20/Apr/2024 13:12:08] "GET / HTTP/1.1" 200 10660
```

![2024-04-20_13h12_12](https://github.com/CristianoSFMothe/healing/assets/68359459/890bda3a-a66d-4e7a-89b0-61fad6b141ea)

## Conceito

Aplicação Web segui uma estrutura `client-server`, onde possui um `cliente` e um `servidor`, onde:

* `servidor` - onde a aplicação fica hospedada, local onde será realizado todos os processamento, validações dos dados, conexão com o banco de dados, manipulação e renderização dos templantes.

* `cliente` - são os Notebooks, computadores, smartphones, ou seja quem está acessando nosso site ou aplicação.

![image](https://github.com/CristianoSFMothe/healing/assets/68359459/c37c4a59-2440-4df6-843e-df4a435f9ed9)

--

## Cadastro Usuários

```bash
python manage.py startapp usuarios
```

![image](https://github.com/CristianoSFMothe/healing/assets/68359459/d87a8a80-9fda-477c-a679-d32b7f5ab8cf)

1. Dentro da pasta `healing`, no arquivo `urls.py` crie uma URL para o app usuário:

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
]
```

</details>

2. No app usuário crie um arquivo para armazenar e criar as URL's `urls.py`:

<details><summary>Visualizar código</summary>

```python
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
]

```

</details>

3. Na pasta `healing` no arquivo `settings.py`, tem que informar para o Django que a pasta `usuarios`, e um novo app Django para instalar.

<details><summary>Visualizar código</summary>

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios'
]
```

</details>

4. Em `usuarios` no arquivo `views.py` crie a view cadastro:

<details><summary>Visualizar código</summary>

```python
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
```

</details>

5. Configure onde o Django deve buscar por arquivos de templates, dentro do arquivo `settings.py`: 

<details><summary>Visualizar código</summary>

```python
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

</details>

### Arquivo base para o HTML

Na raiz do projeto, criar uma pasta `templates`, dentro dessa pasta criar o `base.html`:

<details><summary>Visualizar código</summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="">
    <title>{% block 'title' %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block 'head' %}{% endblock 'head' %}
  </head>
  <body>
    {% block 'body' %}{% endblock 'body' %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

</details>

### Configuração do HTML da página de cadastro

1. Editar o arquivo `views` dentro do `app cadastro`

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
  return render(request, 'cadastro.html')

```

</details>

2. Dentro da `app usuarios`, criar uma pasta `templates`, com o arquivo `cadastro.html`

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %} {% block 'body' %}

<div class="container-fluid">
  <div class="row">
    <div class="col-md d-flex justify-content-center">
      <div class="cont-cadastro">
        <br />
        <br />
        <section class="cont-logo">
          <img class="logo" src="#" />
          <label class="text-logo">HEALING</label>
        </section>
        <hr />

        <form action="" method="post">
          <h2 class="fonte-destaque1">Cadastre-se</h2>
          <br />
          <label for="">Username</label>
          <input
            type="text"
            name="username"
            id="username"
            class="form-control"
            placeholder="Username ..."
          />
          <br />
          <label for="">E-mail</label>
          <input
            type="text"
            name="email"
            id="email"
            placeholder="email@email.com"
            class="form-control"
          />
          <br />
          <div class="row">
            <div class="col-md">
              <label for="">Senha</label>
              <input
                type="password"
                name="senha"
                id="senha"
                class="form-control"
                placeholder="Digite sua senha ..."
              />
            </div>
            <div class="col-md">
              <label for="">Confirmar senha</label>
              <input
                type="password"
                name="confirmar_senha"
                id="confirmar_senha"
                class="form-control"
                placeholder="Digite sua senha novamente ..."
                id=""
              />
            </div>
          </div>
          <br />

          <input
            type="submit"
            value="Cadastrar"
            id="btn_cadastrar"
            class="btn btn-success btn-dark-color"
          />
          <a href="#" class="btn btn-dark-color-outline" id="btn_possui_conta">Já possuo uma conta</a>
        </form>
      </div>
    </div>
    <div
      class="col-md bg-main d-flex justify-content-center align-items-center"
    >
      <img src="#" alt="" />
    </div>
  </div>
</div>

{% endblock 'body' %}

```

</details>

3. Configure os arquivos estáticos, no core do projeto na pasta `healing`, editar os arquivos estáticos dentro do arquivo `settings.py`:

<details><summary>Visualizar código</summary>

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

</details>

4. Na pasta `templates` criar a pasta `static`, dentro dela criar a pasta `usuarios`. E dentro da pasta `usuarios` criar a subpasta `css` e outra `js`. Criar também uma pasta `geral`, com as subpastas `css` e `js`

```
|- templates
| |- static
| |  |- geral
| |  | |- css
| |  | |- | base.css
| |  | |- js
```

Dento da pasta `css` na pasta `geral`, criar um arquivo `base.css`:

<details><summary>Visualizar código</summary>

```css
:root{     
  --main-color: #00CCBE;
  --dark-color: #09A6A3;
  --contrast-color: #FFD686;
}

.bg-color-dark{
  background-color: var(--main-color);
}

.p-bold{
  font-weight: bold;
}

.color-dark{
  color: var(--dark-color);
}
```

</details>

5. No arquivo `base.html` na pasta `templates` na raiz do projeto, chamar a tag link do HTML:

<details><summary>Visualizar código</summary>

```html	
<link rel="stylesheet" href="{% static 'geral/css/base.css' %}">
```

</details>

6. Agora na pasta `templates` dentro da pasta `static`, criar uma pasta `usuarios`. E criar aa subpastas `css` e `js`.

```
|- templates
| |- static
| |  |- geral
| |  | |- css
| |  | |- js
| |  |- usuarios
| |  | |- css
| |  | |- | usuarios.css
| |  | |- js
```

Na pasta `templates`, dentro da `usuarios/css` criar o `usuarios.css`

<details><summary>Visualizar código</summary>

```css
.bg-main{
  background-color: var(--main-color);
  height: 100vh;
}

.cont-cadastro{
  width: 60%;
}

.cont-logo{
  text-align: center;
}

.text-logo{
  font-size: 30px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.fonte-destaque1{
  color: var(--dark-color)
}

.btn-dark-color{
  background-color: var(--dark-color);
  color: white;
}

.btn-dark-color-outline{
  border: 1px solid var(--dark-color);
  color: var(--dark-color)
}

.btn-dark-color-outline:hover{
  background-color: var(--dark-color);
  color: white;
  border: 1px solid var(--dark-color);
}
```

</details>

7. No `app usuarios`em `cadastro.html` importe o `usuarios.css`

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %}
{% load static %}

{% block 'head' %}
    <link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}">
{% endblock 'head' %}

{% block 'body' %}
```
</details>

## Criação da migration

O Django já trás na sua criação uma serie de estruturas de banco de dados, mas para fazer com que os mesmo sejam ativos é necessário executar a `migration`

```bash
python .\manage.py migrate

# Resposta do comando
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### Configurando a views de cadastro do usuários

1. Altere o arquivo `views` do `app usuários`:

<details><summary>Visualizar código</summary>

```python
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
```

</details>

2. No `form` de usuário, dentro do arquivo `views`, alterar para a seguinte estrutura:

```html	
<form action="{% url "cadastro" %}" method="POST">{% csrf_token %}
```

## Configuração das mensagens

1. No arquivo `settings.py`, na pasta `healing`, criar o arquivo:

```python
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}
```

2. Configure no arquivo `views.py`, do `app usuarios`:

<details><summary>Visualizar código</summary>

```python	
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
```

</details>

3. Renderize as mensagens no HTML, dentro do `app usuarios` na pasta `templates/cadastro.html`:

<details><summary>Visualizar código</summary>

```python	
{% if messages %}
  {% for message in messages %}
      <section class="alert {{message.tags}}">
          {{message}}
      </section>
    {% endfor %}
{% endif %}
```
</details>

## Login

1. No arquivo `urls.py` no `app usuarios`, criar uma nova URL para login:

<details><summary>Visualizar código</summary>

```python	
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
]
```
</details>

2. No arquivo `views.py` no `app usuarios`, criar a função:

<details><summary>Visualizar código</summary>

```python	
def login_view(request):
  if request.method == 'GET':
    return render(request, 'login.html')  
```
</details>

3. Na pasta `templates` no `app usuarios`, criar um novo arquivo `login.html`:

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %} {% load static %} {% block 'head' %}
<link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}" />
{% endblock 'head' %} {% block 'body' %}

<div class="container-fluid">
  <div class="row">
    <div class="col-md d-flex justify-content-center">
      <div class="cont-cadastro">
        <br />
        <br />
        <section class="cont-logo">
          <img class="logo" src="{% static 'geral/img/logo.png' %}" />
          <label class="text-logo">HEALING</label>
        </section>
        <hr />

        <form action="#" method="POST">
          <h2 class="fonte-destaque1">Logar</h2>
          {% if messages %}
          <br />
          {% for message in messages %}
          <section class="alert {{message.tags}}">{{message}}</section>
          {% endfor %} {% endif %}
          <br />
          <label for="">Username</label>
          <input
            type="text"
            name="username"
            id="username"
            class="form-control"
            placeholder="Username ..."
          />
          <br />

          <label for="">Senha</label>
          <input
            type="password"
            name="senha"
            id="senha"
            class="form-control"
            placeholder="Digite sua senha ..."
          />
          <br />

          <input
            type="submit"
            value="Logar"
            id="btn_login"
            class="btn btn-success btn-dark-color"
          />
          <a
            href="{% url 'cadastro' %}"
            id="btn_cadastro"
            class="btn btn-dark-color-outline"
            >Não possuo uma conta</a
          >
        </form>
      </div>
    </div>
    <div
      class="col-md bg-main d-flex justify-content-center align-items-center"
    >
      <img src="{% static 'usuarios/img/ilustracao.png' %}" alt="" />
    </div>
  </div>
</div>

{% endblock 'body' %}

```
</details>

4. Configurar o `form` do `login.html` e o botão `possui uma conta` do `cadastro.html`:

<details><summary>Visualizar código</summary>

```html	
# Form login.html
<form action="{% url "login" %}" method="POST">{% csrf_token %}

# Botão possui uma conta cadastro.html
<a href="{% url 'login' %}" class="btn btn-dark-color-outline">Já possuo uma conta</a>
``` 
</details>

5. Alterando a função `login_view`:

<details><summary>Visualizar código</summary>

```python	
from django.contrib import auth

def cadastro(request):
  ...

def login_view(request):
  if request.method == 'GET':
    return render(request, 'login.html')    
  elif request.method == 'POST':
    userrname = request.POST.get('username')
    senha = request.POST.get('senha')    

  user = auth.authenticate(request, username=userrname, password=senha)
  
  if user:
    auth.login(request, user)
    return redirect('/pacientes/home')
  
  messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
  return redirect('/usuarios/login')
```

</details>

## Logout

1. Criar a URL de logout, no arquivo `urls.py` dentro do `app usuarios`:

<details><summary>Visualizar código</summary>

```python	
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('sair/', views.sair, name="sair"),    
]
```

</details>

2. No arquivo `views.py` dentro do `app usuarios` criar a função:

<details><summary>Visualizar código</summary>

```python
def sair(request):
  auth.login(request)
  return redirect('/usuarios/login')

```

</details>

## Médico

1. Criação de um novo app chamado `medico`:

```bash
python manage.py startapp medico
```

2. Na pasta `settings.py` no core da aplicação da pasta `healing`, realizar a instalação do novo app criado:

<details><summary>Visualizar código</summary>

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'medico'
]
```

</details>

3. Em `models.py` dentro do `app medico`, crie a tabela no banco para salvar as informações de médico:

<details><summary>Visualizar código</summary>

```python
class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidade
```

</details>

4. Executando as migration:

```bash
python manage.py makemigrations

# Resposta do comando executado com sucesso
Migrations for 'medico':
  medico\migrations\0001_initial.py
    - Create model Especialidades
```

```bash
python manage.py migrate

# Resposta do comando executado com sucesso
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, medico, sessions
Running migrations:
  Applying medico.0001_initial... OK
```

5. Criação do usuário administrativo:

```bash
python manage.py createsuperuser

# Resposta do comando executado com sucesso
Usuário (leave blank to use 'mothe'): mothe # nome do usuário
Endereço de email: # email pode deixar vazio
Password: # informar a senha
Password (again): # confirmar a senha
Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.
Esta senha é muito comum.
Esta senha é inteiramente numérica.
Bypass password validation and create user anyway? [y/N]: y # caso a senha senha uma senha fraca irá perdi a confirmação
Superuser created successfull
```

Execute o servidor novamente com o comando `python manage.py runserver` e acesse a rota administrativa.

=== imagem 1 ===

=== imagem 2 ===

6. No arquivo `admin.py` dentro do `app medico`, cadastrar o banco de dados criado de `Especialidades`, para está visível dentro da área administrativa.

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from .models import Especialidades

admin.site.register(Especialidades)
```

</details>

=== imagem 3 ===

=== imagem 4 ===

### Criação da tabela dados médicos

1. Criação da tabela de dados médicos, dentro do arquivo `models.py` do `app medico`:

<details><summary>Visualizar código</summary>

```python
from django.contrib.auth.models import User

class DadosMedico(models.Model):
    crm = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to="rgs")
    cedula_identidade_medica = models.ImageField(upload_to='cim')
    foto = models.ImageField(upload_to="fotos_perfil")
    descricao = models.TextField()
    valor_consulta = models.FloatField(default=100)
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username
```

</details>

2. Com a estrutura da tabela criada, com o servidor parado, executar as migration:

```bash
python manage.py makemigrations

# Resposta do comando executado com sucesso
Migrations for 'medico':
  medico\migrations\0002_dadosmedico.py
    - Create model DadosMedico
```

```bash
python manage.py migrate

# Resposta do comando executado com sucesso
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, medico, sessions
Running migrations:
  Applying medico.0002_dadosmedico... OK
```

3. Ativar também a tabela dados médico dentro da área administrativa:

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from .models import Especialidades, DadosMedico

admin.site.register(Especialidades)
admin.site.register(DadosMedico)
```

</details>

### Configuração da página de médicos

1. Dentro da pasta `healing` no arquivo `urls.py` criar a URL para o `app medico`:

```python
path('medicos/', include('medico.urls')),
```

2. No `app medico`, criar um novo arquivo `urls.py`:

<details><summary>Visualizar código</summary>

```python
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_medico/', views.cadastro_medico, name="cadastro_medico"),
]
```

</details>

3. No `app medico`, no arquivo `views.py`, criar a função:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render

# Create your views here.
def cadastro_medico(request):
    if request.method == "GET":
        return render(request, 'cadastro_medico.html')
```

</details>

4. No `app medico` criar uma pasta `templates`, com o arquivo `cadastro_medico.html`:

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %} {% load static %} {% block 'head' %}
<link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}" />

{% endblock 'head' %} {% block 'body' %}

<div class="container">
  <br />
  <br />
  <div class="row">
    <div class="col-md-8">
      <p class="p-bold">Olá, <span class="color-dark"></span></p>
      <p class="p-bold">Vamos realizar seu cadastro médico legal.</p>
      {% if messages %}
      <br />
      {% for message in messages %}
      <section class="alert {{message.tags}}">{{message}}</section>
      {% endfor %} {% endif %}
      <br />
      <form action="#" method="post" enctype="multipart/form-data">
        <div class="row">
          <div class="col-md">
            <label for="">CRM:</label>
            <input
              type="text"
              class="form-control shadow-main-color"
              name="crm"
              id="crm"
              placeholder="CRM..."
            />
          </div>
          <div class="col-md">
            <label for="">Cédula de identidade médica:</label>
            <input
              type="file"
              name="cim"
              id="cim"
              class="form-control shadow-main-color"
            />
          </div>
        </div>
        <br />
        <div class="row">
          <div class="col-md">
            <label for="">Nome completo:</label>
            <input
              type="text"
              class="form-control shadow-main-color"
              name="nome"
              id="nome"
              placeholder="Digite seu nome ..."
            />
          </div>
          <div class="col-md">
            <label for="">CEP</label>
            <input
              type="text"
              name="cep"
              id="cep"
              class="form-control shadow-main-color"
            />
          </div>
        </div>
        <br />
        <label for="">Rua</label>
        <input
          type="text"
          name="rua"
          id="rua"
          class="form-control shadow-main-color"
          placeholder="Endereço ..."
        />
        <br />
        <div class="row">
          <div class="col-md">
            <label for="">Bairro:</label>
            <input
              type="text"
              class="form-control shadow-main-color"
              name="bairro"
              id="bairro"
              placeholder="Bairro ..."
            />
          </div>
          <div class="col-md">
            <label for="">Número:</label>
            <input
              type="number"
              name="numero"
              id="numero"
              class="form-control shadow-main-color"
            />
          </div>
        </div>
        <br />
        <label for="">RG:</label>
        <input
          type="file"
          name="rg"
          id="rg"
          class="form-control shadow-main-color"
        />
        <br />
        <label for="">Foto de perfil:</label>
        <input
          type="file"
          name="foto"
          id="foto"
          class="form-control shadow-main-color"
        />
        <br />
        <label for="">Especialidade médica</label>
        <select name="especialidade" class="form-select" id="">
          <option value="">X</option>
        </select>
        <br />
        <label for="">Descrição:</label>
        <textarea
          name="descricao"
          id="descricao"
          class="form-control shadow-main-color"
        ></textarea>
        <br />
        <label for="">Valor consulta:</label>
        <input
          type="number"
          name="valor_consulta"
          id="valor_consulta"
          class="form-control shadow-main-color"
        />
        <br />
        <input
          type="submit"
          value="Cadastre-se"
          id="btn_cadastre_se"
          class="btn btn-success btn-dark-color"
        />
      </form>
    </div>
    <div class="col-md-4"></div>
  </div>
</div>

{% endblock 'body' %}
```

</details>

5. Na pasta `templates` na raiz do projeto, criar a estrutura:

```
|- templates
| |- static
| |  |- geral
| |  | |- css
| |  | |- js
| |  |- usuarios
| |  | |- css
| |  | |- | usuarios.css
| |  | |- img
| |  | |- js
| |  |- medicos
| |  | |- css
| |  | |- | cadastro_medico.css
| |  | |- img
| |  | |- js
```

6. Criar o arquivo `cadastro_medico.css`:

<details><summary>Visualizar código</summary>

```css
.shadow-main-color{
    box-shadow: 1px 1px 5px 1px rgba(0, 204, 190,.4);
}
```

</details>

7. Importar o `CSS` no `HTML` no `app medico` dentro da pasta `template/cadastro_medico.html`:

<details><summary>Visualizar código</summary>

```html
<link rel="stylesheet" href="{% static 'medicos/css/cadastro_medico.css' %}">
```

</details>

8. Estilizando o nome, no arquivo `cadastro_medico.html`, editar o tag `p` do nome

<details><summary>Visualizar código</summary>

```html
<p class="p-bold">Olá, <span class="color-dark">{{request.user.username}}</span></p>
```

</details>

9. Direcionando o `form` do `app medico` para a URL respectiva:

<details><summary>Visualizar código</summary>

```html
<form action="{% url 'cadastro_medico' %}" method="post" enctype='multipart/form-data'>{% csrf_token %}
```

</details>

## Configurando a seleção da especialidade

1. Editar o arquivo `views.py` do `app medico`:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render
from .models import Especialidades

# Create your views here.
def cadastro_medico(request):
    if request.method == "GET":
      especialidade = Especialidades.objects.all()
      return render(request, 'cadastro_medico.html', {'especialidade': especialidade})
```

</details>

2. Recuperando dinamicamente as especialidades médicas cadastradas no banco de dados:

<details><summary>Visualizar código</summary>

```html
<select name="especialidade" class="form-select" id="">
  <option disabled selected>Escolha uma especialidade</option>
  {% for i in especialidades %}
      <option value="{{ i.id }}">{{ i.especialidade }}</option>
  {% endfor %}
</select>
```

</details>

3. Configuração da função da `views.py` do `cadastro_medico`:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages import constants

# Create your views here.
def cadastro_medico(request):
    if request.method == "GET":
      especialidades = Especialidades.objects.all()
      return render(request, 'cadastro_medico.html', {'especialidades': especialidades})
    elif request.method == "POST":
      crm = request.POST.get('crm')
      nome = request.POST.get('nome')
      cep = request.POST.get('cep')
      rua = request.POST.get('rua')
      bairro = request.POST.get('bairro')
      numero = request.POST.get('numero')
      cim = request.FILES.get('cim')
      rg = request.FILES.get('rg')
      foto = request.FILES.get('foto')
      especialidade = request.POST.get('especialidade')
      descricao = request.POST.get('descricao')
      valor_consulta = request.POST.get('valor_consulta')
      
    #TODO: Validar todos os campos

    dados_medico = DadosMedico(
        crm=crm,
        nome=nome,
        cep=cep,
        rua=rua,
        bairro=bairro,
        numero=numero,
        rg=rg,
        cedula_identidade_medica=cim,
        foto=foto,
        user=request.user,
        descricao=descricao,
        especialidade_id=especialidade,
        valor_consulta=valor_consulta,
        user=request.user
    )
    
    dados_medico.save()
    
    messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso.')

    return redirect('/medicos/abrir_horario')

```

</details>

Criar uma função para validar se o usuário que está acessando a aplicação já e um médico cadastrado.

4. Dentro do `app medicos` no arquivo `models.py` criar a seguinte função:

<details><summary>Visualizar código</summary>

```python
def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()
```

</details>

5. Dentro do arquivo `viws.py` no `app medico`, utilizar a função:

<details><summary>Visualizar código</summary>

```python
from .models import Especialidades, DadosMedico, is_medico

if is_medico(request):
      messages.add_message(request, constants.WARNING, 'Você já é um médico cadastrado.')
      return redirect('/medico/abrir_horario')
```

</details>

## Data abertas

1. No `app medico`, criar uma nova nova classe, para representar um tabela no arquivo `models.py`:

<details><summary>Visualizar código</summary>

```python
class DatasAbertas(models.Model):
    data = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    agendado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.data)
```

</details>

2. Realizar as migrações:

Executando as migration:

```bash
python manage.py makemigrations

# Resposta do comando executado com sucesso
Migrations for 'medico':
  medico\migrations\0003_datasabertas.py
    - Create model DatasAbertas

python manage.py migrate

# Resposta do comando executado com sucesso
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, medico, sessions
Running migrations:
  Applying medico.0003_datasabertas... OK
```

3. Criar a URL para a rota `abrir_horario`, no `app medico` no arquivo `urls.py`:

<details><summary>Visualizar código</summary>

```python
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_medico/', views.cadastro_medico, name="cadastro_medico"),
    path('abrir_horario/', views.abrir_horario, name="abrir_horario"),
]
```

</details>

4. No arquivo de `views.py` no `app medico`, criar a função para a rota de `abrir_horario`:

<details><summary>Visualizar código</summary>

```python
def abrir_horario(request):
    if not is_medico(request.user):
      messages.add_message(request, constants.WARNING, 'Somente médicos podem abrir horário.')
      return redirect('/usuarios/sair')
    
    if request.method == 'GET':
      return render(request, 'abrir_horario.html')
```

</details>

5. Criar em templates o arquivo `abrir_horario.html`, para renderizar a página de `abrir_horario`:

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %} {% load static %} {% block 'head' %}
<link rel="stylesheet" href="{% static 'medicos/css/abrir_horario.css' %}" />
<link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}" />
<link rel="stylesheet" href="{% static 'medicos/css/cadastro_medico.css' %}" />
{% endblock 'head' %} {% block 'body' %}

<div class="container">
  <br /><br />

  <div class="row">
    <div class="col-md-8">
      <img src="" class="foto-perfil" alt="" />
      <label style="margin-left: 30px; font-size: 25px" class="p-bold"
        >Olá, <span class="color-dark">{{request.user.username}}</span></label
      >

      <br />
      {% if messages %}
      <br />
      {% for message in messages %}
      <section class="alert {{message.tags}}">{{message}}</section>
      {% endfor %} {% endif %}
      <br />
      <p style="font-size: 25px" class="p-bold">
        Abrir horários para consultas
      </p>
      <hr />
      <form action="#" method="POST">
        <label for="">Escolher data:</label>
        <input
          type="datetime-local"
          name="data"
          class="form-control shadow-main-color"
        />
        <br />
        <input
          type="submit"
          value="Salvar"
          class="btn btn-success btn-dark-color"
        />
      </form>
    </div>
    <div class="col-md-4">
      <p style="font-size: 25px" class="p-bold">Seus horários:</p>
      <ul class="list-group">
        <li>X</li>
      </ul>
    </div>
  </div>
</div>

{% endblock 'body' %}
```

</details>

6. Recuperando a foto do médico na página de `Abrir Horários`:

<details><summary>Visualizar código</summary>

```python
if request.method == 'GET':
        dados_medico = DadosMedico.objects.get(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medico': dados_medico})
```

</details>

7. Criação da URL para exibição das mídias, editar o arquivo `urls.py` dentro do pasta `healing`:

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('medicos/', include('medico.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

</details>

8. Editando o `HTML` para exibição da imagem do perfil do usuário. No arquivo `abrir_horario.html`:

<details><summary>Visualizar código</summary>

```html
<img src="{{ dados_medico.foto.url }}" class="foto-perfil" alt="foto de perfil do médico" />
```

</details>

9. Criar dentro da pasta `templates` na raiz do projeto, dentro do caminho `templates/static/medicos/css`, criar uma arquivo `abrir_horario.css`:

<details><summary>Visualizar código</summary>

```css
.foto-perfil{
    width: 150px;
    height: 150px;
    border-radius: 75px;
}
```

</details>

10. Editar o `form` da página de `abrir_horario.html`:

<details><summary>Visualizar código</summary>

```html
<form action="{% url "abrir_horario" %}" method="POST">{% csrf_token %}
```

</details>

11. Atualizando a função de `abrir_horario`:

<details><summary>Visualizar código</summary>

```python
from .models import Especialidades, DadosMedico, is_medico, DatasAbertas
from django.contrib.messages import constants
from datetime import datetime

def abrir_horario(request):
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING,
                             'Somente médicos podem abrir horário.')
        return redirect('/usuarios/sair')

    if request.method == 'GET':
        dados_medico = DadosMedico.objects.get(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medico': dados_medico})
      
    elif request.method == 'POST':
      data = request.POST.get('data')      
      data_formatada = datetime.strptime(data, '%Y-%m-%dT%H:%M')
      
      if data_formatada <= datetime.now():
        messages.add_message(request, constants.WARNING, 'A data não pode ser anterior a data atual.')
        return redirect('/medicos/abrir_horario')
      
      horario_abrir = DatasAbertas(
        data=data,
        user=request.user
      )
      
      horario_abrir.save()
      
      messages.add_message(request, constants.SUCCESS, 'Horaio cadastrado com sucesso.')
      
      return redirect('/medicos/abrir_horario')

```

</details>

12. Filtrando as datas aberta do usuário logado:

<details><summary>Visualizar código</summary>

```python
 if request.method == 'GET':
        dados_medico = DadosMedico.objects.get(user=request.user)
        datas_abertas = DatasAbertas.objects.filter(user=request.user)
        return render(request, 'abrir_horario.html', {
          'dados_medico': dados_medico,
          'datas_abertas': datas_abertas
          })
```

</details>

13. Editando o `settings.py` do core do projeto para não utilizar o **timezone** `USE_TZ = False`

14. Editando o arquivo `abrir_horario.html` para no `li` exibir os horários abertos:

<details><summary>Visualizar código</summary>

```html
<ul class="list-group">
        
  {% for data in datas_abertas %}
    <li>{{data}}</li>          
  {% endfor %}
  
</ul>
```

</details>

## Pacientes

1. Crie um APP para os pacientes:

```python
python manage.py startapp paciente
```

2. Instalar o `app pacientes` no core do projeto na pasta `healing` no arquivo `settings.py`:

<details><summary>Visualizar código</summary>

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'medico',
    'paciente'
]
```

</details>

3. Criar uma nova **URL** no arquivo `healing/settings.py`:

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('medicos/', include('medico.urls')),
    path('pacientes/', include('paciente.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

</details>

4. No `app paciente`, criar um novo arquivo `urls.py`:

<details><summary>Visualizar código</summary>

```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home')
]
```

</details>

5. No arquivo `views.py`, criar a função para renderizar a página `home.html`:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render

def home(request):
  if request.method == 'GET':
    return render(request, 'home.html')
```

</details>

6. Dentro do `app paciente` criar a pasta `templates` com o arquivo `home.html`:

<details><summary>Visualizar código</summary>

```html
{% extends "base.html" %} {% load static %} {% block 'head' %}
<link rel="stylesheet" href="{% static 'medicos/css/abrir_horario.css' %}" />
<link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}" />
<link rel="stylesheet" href="{% static 'medicos/css/cadastro_medico.css' %}" />
<link rel="stylesheet" href="{% static 'pacientes/css/home.css' %}" />
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
/>
{% endblock 'head' %} {% block 'body' %}

<br /><br />

<div class="container">
  <div class="row">
    <div class="col-md-8">
      <p style="font-size: 25px" class="p-bold">
        Olá, <span class="color-dark">{{request.user.username}}.</span>
      </p>
      <form action="" post="GET">
        <input
          type="text"
          class="form-control shadow-main-color"
          placeholder="Busque por profissionais ..."
          name="medico"
        />
        <br />

        <div class="especialidades">
          <input type="checkbox" name="especialidades" value="" />
          <span class="badge bg-secondary"> Especialidade X </span>
        </div>
        <br />
        <input
          type="submit"
          value="filtrar"
          class="btn btn-success btn-dark-color"
        />
      </form>
      <hr />

      <div class="list-medicos">
        <div class="card-medicos shadow-main-color">
          <div class="row">
            <div class="col-md-3">
              <img src="#" class="foto-perfil-card" alt="" />
            </div>
            <div class="col-md">
              <p style="font-size: 20px" class="p-bold">
                Dr(a). Nome aqui
                <i class="bi bi-patch-check-fill icon-main"></i>
              </p>
              <p>Descrição aqui</p>
            </div>
          </div>
          <p><i class="bi bi-map icon-main"></i>&nbsp&nbspRua tal aqui, 000.</p>
          <p>
            <i class="bi bi-calendar2-week icon-main"></i>&nbsp&nbspProxima
            data: 00/00/0000

            <a href="#" class="btn btn-success btn-dark-color">Agendar</a>
          </p>
        </div>

        <br />
      </div>
    </div>
    <div class="col-md-4">
      <p style="font-size: 25px" class="p-bold">Lembretes</p>

      <p class="bg-main-lembrete">
        <span class="p-bold"
          ><i class="bi bi-exclamation-triangle-fill icon-differential"></i
          >&nbsp&nbsp Consulta com Pedro Sampario em 7 dias.</span
        >
      </p>
    </div>
  </div>
</div>

{% endblock 'body' %}

```

</details>

7. Criar dentro da pasta `templates` na raiz do projeto uma estrutura para o `app pacientes`, criando as seguintes pasta dentro de `static`, criar uma pasta para `pacientes` e as subpastas `css` e `js`:

```
|- templates
| |- static
| |  |- pacientes
| |  | |- css
| |  | | |- home.css
| |  | |- js
```

<details><summary>Visualizar código</summary>

```css
.especialidades {
  font-size: 20px;
}

.card-medicos {
  width: 60%;
  background-color: #eaeaea;
  border: 1px solid var(--main-color);
  padding: 20px;
}

.foto-perfil-card {
  width: 90px;
  height: 90px;
  border-radius: 45px;
}

.foto-perfil-card-lg {
  width: 180px;
  height: 180px;
  border-radius: 90px;
}
.icon-main {
  color: var(--main-color);
}

.bg-main-lembrete {
  background-color: var(--dark-color);
  padding: 10px;
  color: white;
}

.icon-differential {
  color: var(--contrast-color);
}

table {
  border-collapse: collapse !important;
  width: 100%;
}

th,
td {
  padding: 8px;
  text-align: center;
  background-color: #eaeaea !important;
}

th {
  background-color: #eaeaea;
}

.link {
  text-decoration: none;
}

.today {
  background-color: var(--dark-color);
}

.selecionar-dia {
  width: 100%;
  background-color: #eaeaea;
  box-shadow: 1px 1px 10px gray;
}

.header-dias {
  background-color: var(--dark-color);
  padding: 15px;
  color: white;
  text-decoration: none;
}

.dia-semana {
  float: right;
}

.conteudo-data {
  padding: 15px;
  color: black;
}

.link:hover {
  text-decoration: none;
}

.list-minhas-consultas {
  background-color: #eaeaea;

  padding: 10px;
}

.documentos {
  background-color: #cfcfcf;
  color: black;
  padding: 20px;
  border-radius: 10px;
  font-size: 20px;
}

```

</details>

### Lista médicos na página de pacientes

1. Na `views.py` no `app pacientes`, buscar todos os médicos:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render
from medico.models import DadosMedico


def home(request):
  if request.method == 'GET':
    medicos = DadosMedico.objects.all()
    return render(request, 'home.html', { 'medicos': medicos})


```
</details>

2. Recuperar os dados dinamicamente do banco de dados:

<details><summary>Visualizar código</summary>

```html	
<div class="list-medicos">
  {% for medico in medicos %}

  <div class="card-medicos shadow-main-color">
    <div class="row">
      <div class="col-md-3">
        <img
          src="{{medico.foto.url}}"
          class="foto-perfil-card"
          alt="{{medico.nome}}"
        />
      </div>
      <div class="col-md">
        <p style="font-size: 20px" class="p-bold">
          Dr(a). {{medico.nome}}
          <i class="bi bi-patch-check-fill icon-main"></i>
        </p>
        <p>{{medico.descricao}}</p>
      </div>
    </div>
    <p><i class="bi bi-map icon-main"></i>&nbsp&nbsp{{medico.rua}}</p>
    <p>
      <i class="bi bi-calendar2-week icon-main"></i>&nbsp&nbspProxima
      data: {% if medico.proxima_data %} {{medico.proxima_data}} {% else
      %} Aguarde abertura de uma data... {% endif %}

      <a href="#" class="btn btn-success btn-dark-color">Agendar</a>
    </p>
  </div>

  <br />

  {% endfor %}
</div>
```

</details>

3. Criar uma `property` dentro do arquivo de `models.py` do `app medicos`:

<details><summary>Visualizar código</summary>

```python
@property
    def proxima_data(self):
        proxima_data = DatasAbertas.objects.filter(user=self.user).filter(
            data__gt=datetime.now()).filter(agendado=False).order_by('data').first()

        return proxima_data
```

</details>

4. Cadastrar os `DadasAbertas` no admin do do `app medico`:

<details><summary>Visualizar código</summary>

```python
from django.contrib import admin
from .models import Especialidades, DadosMedico, DatasAbertas

admin.site.register(Especialidades),
admin.site.register(DadosMedico),
admin.site.register(DatasAbertas),

```


### Listando especialidade

1. Editar a `views.py` do `app paciente`:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render
from medico.models import DadosMedico, Especialidades

def home(request):
    if request.method == 'GET':
        medicos = DadosMedico.objects.all()
        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos': medicos, 'especialidades': especialidades})
```

</details>

2. Editar o arquivo `home.html` do `app paciente`, para lista as especialidades e adicionar a URL na `action` do formulário:

<details><summary>Visualizar código</summary>

```html	
<form action="{% url 'home' %}" post="GET">

{% for especialidade in especialidades %}
  <input type="checkbox" name="especialidades" value="" />
  <span class="badge bg-secondary"> {{especialidade.especialidade}} </span>
{% endfor %} 
```
</details>

3. Filtrando por especialidades, editar o arquivo de `views.py` do `app pacientes`:

<details><summary>Visualizar código</summary>

```python
from django.shortcuts import render
from medico.models import DadosMedico, Especialidades

def home(request):
    if request.method == 'GET':
        medico_filtar = request.GET.get('medico')
        especialidade_filtar = request.GET.getlist('especialidade')
        
        medicos = DadosMedico.objects.all()
        
        if medico_filtar:
          medicos = medicos.filter(nome__icontains=medico_filtar)     
          
        if especialidade_filtar:
          medicos = medicos.filter(especialidade_id_in=especialidade_filtar)   
      
        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos': medicos, 'especialidades': especialidades})
```

</details>

### Escolhendo horario

<details><summary>Visualizar código</summary>

1. Na `urls.py` do `app paciente`, adicionar uma nova URL:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('escolher_horario/<int:id_dados_medicos>',
         views.escolher_horario, name='escolher_horario')
]
```

</details

2. No arquivo `views.py` do `app paciente`, criar a função:

<details><summary>Visualizar código</summary>

```python
from medico.models import DadosMedico, Especialidades, DatasAbertas
from datetime import datetime

def escolher_horario(request, id_dados_medicos):
    if request.method == 'GET':
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = DatasAbertas.objects.filter(
            user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)

        return render(request, 'escolher_horario.html', {'medico': medico, 'datas_abertas': datas_abertas})
```

</details>

3. Na pasta templates criar um novo arquivo `escolher_horario.html`:

<details><summary>Visualizar código</summary>

```html	
{% extends "base.html" %} {% load static %} {% block 'head' %}

<link rel="stylesheet" href="{% static 'medicos/css/abrir_horario.css' %}" />
<link rel="stylesheet" href="{% static 'usuarios/css/usuarios.css' %}" />
<link rel="stylesheet" href="{% static 'medicos/css/cadastro_medico.css' %}" />
<link rel="stylesheet" href="{% static 'pacientes/css/home.css' %}" />
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
/>

{% endblock 'head' %} {% block 'body' %}

<div class="container">
  <br /><br />

  <div class="row">
    <div class="col-md-8">
      <div class="row">
        <div class="col-md-3 foto-card">
          <img src="{{medico.foto.url}}" class="foto-perfil-card" alt="Dr(a) {{medico.nome}}" />
        </div>
        <div class="col-md dados-card">
          <p style="font-size: 20px" class="p-bold nome">
            Dr(a). {{medico.nome}} <i class="bi bi-patch-check-fill icon-main"></i>
          </p>
          <p class="descricao">{{medico.descricao}}</p>
        </div>
      </div>
      <br />
      {% if messages %}
      <br />
      {% for message in messages %}
      <section class="alert {{message.tags}}">{{message}}</section>
      {% endfor %} {% endif %}

      <hr />

      <div class="row">
        
        {% for data_aberta in datas_abertas %}
          <div class="col-md-3">
            <a class="link" href="">
              <div class="selecionar-dia">
                <div class="header-dias">
                  {% comment %} <span class="mes"> {{data_aberta.data.month}} </span> {% endcomment %}
                  <span class="mes"> {{ data_aberta.data|date:"F" }} </span>

                  <span class="dia-semana"> {{ data_aberta.data|date:"l" }} </span>
                </div>

                <div class="conteudo-data">{{data_aberta.data}}</div>
              </div>
            </a>
            <br />
          </div>
          
        {% endfor %}

      </div>
    </div>
    <div class="col-md-4"></div>
  </div>
</div>
{% endblock 'body' %}

```

</details>


4. Editar a URL do botão **Agendar** no arquivo `home.html` do `app paciente`

<details><summary>Visualizar código</summary>

```html	
<a href="{% url 'escolher_horario' medico.id %}" class="btn btn-success btn-dark-color">Agendar</a>
```

</details>

5. Editar o 