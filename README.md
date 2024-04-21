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


# Cadastro Usuários

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

### Configuração das mensagens

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
    
  # Verificar se exite no banco de dados
  user = auth.authenticate(request, username=userrname, password=senha)
  
  if user:
    auth.login(request, user)
    return redirect('/pacientes/home')
  
  messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
  return redirect('/usuarios/login')
```

</details>