from django.shortcuts import render
from medico.models import DadosMedico, Especialidades, DatasAbertas
from datetime import datetime


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
