from django.shortcuts import render, redirect
from medico.models import DadosMedico, Especialidades, DatasAbertas
from datetime import datetime
from .models import Consulta
from django.contrib import messages
from django.contrib.messages import constants

from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        medico_filtar = request.GET.get('medico')
        especialidades_filtar = request.GET.getlist('especialidades')

        medicos = DadosMedico.objects.all()

        if medico_filtar:
            medicos = medicos.filter(nome__icontains=medico_filtar)

        if especialidades_filtar:
            medicos = medicos.filter(
                especialidade_id__in=especialidades_filtar)

        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos': medicos, 'especialidades': especialidades})


def escolher_horario(request, id_dados_medicos):
    if request.method == 'GET':
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = DatasAbertas.objects.filter(
            user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)

        return render(request, 'escolher_horario.html', {'medico': medico, 'datas_abertas': datas_abertas})
      
def agendar_horario(request, id_data_aberta):
  if request.method == 'GET':
    data_aberta = DatasAbertas.objects.get(id=id_data_aberta)
    
    horario_agendado = Consulta(
      paciente=request.user,
      data_aberta=data_aberta,
    )
    
    horario_agendado.save()
    
    data_aberta.agendado = True
    data_aberta.save()
    
    messages.add_message(request, constants.SUCCESS, 'Consulta agendada com sucesso!')
    
    return redirect('/pacientes/minhas_consultas/')
    
    
  
