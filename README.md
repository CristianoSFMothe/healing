# Healing

O Healing e um sistema Web de tele atendimento medico, onde os médicos poderão de se cadastrar assim como o pacientes, e os médicos poderão realizar o atendimento, abrir seus horários para atendimento, visualizar o dashboards

## Design

O **Healing** e um sistema de tele medicina que, no qual foi criado de acordo com a estrutura do design, que poder ser visualizando no <a href="https://www.figma.com/file/g7xzaMum3AWGnP1B52tRLR/Healing?type=design&node-id=0%3A1&mode=dev&t=2ChGg41zQRcFMVDT-1" target="_blank">Figma</a>

## Pre-requisitos

* Necessário ter o <a href="https://www.python.org/" target="_blank">Python</a>
* Com o framework do <a href="https://www.djangoproject.com/" target="_blank">Django</a>

## Estrutura HTTP Response

![image](https://github.com/CristianoSFMothe/healing/assets/68359459/ec4e876c-8574-4dd1-9ec4-c40bc2d69536)

![image](https://github.com/CristianoSFMothe/healing/assets/68359459/17b4c142-8289-4fa3-9e63-9a7ddab8a769)

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

## Conceito

Aplicação Web segui uma estrutura `client-server`, onde possui um `cliente` e um `servidor`, onde:

* `servidor` - onde a aplicação fica hospedada, local onde será realizado todos os processamento, validações dos dados, conexão com o banco de dados, manipulação e renderização dos templantes.

* `cliente` - são os Notebooks, computadores, smartphones, ou seja quem está acessando nosso site ou aplicação.

==== IMAGEM DO CONCEITO REQUEST 1 =====


# Cadastro Usuários

```bash
python manage.py startapp usuarios
```

==== IMAGEM DO CONCEITO REQUEST 2 =====


