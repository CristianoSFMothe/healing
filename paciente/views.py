from django.shortcuts import render
from medico.models import DadosMedico, Especialidades

def home(request):
    if request.method == 'GET':
        medico_filtar = request.GET.get('medico')
        especialidades_filtar = request.GET.getlist('especialidades')
        
        medicos = DadosMedico.objects.all()
        
        if medico_filtar:
          medicos = medicos.filter(nome__icontains=medico_filtar)     
          
        if especialidades_filtar:
          medicos = medicos.filter(especialidade_id__in=especialidades_filtar)   
      
        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos': medicos, 'especialidades': especialidades})
