from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Especialidad, Medico
from .serializers import EspecialidadSerializer, MedicoSerializer
from rest_framework import viewsets



# Create your views here.
def angular_app(request):
    return render(request, 'index.html')

@api_view(['GET'])
def listar_especialidades(request):
    especialidades = Especialidad.objects.all()
    serializer = EspecialidadSerializer(especialidades, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def medicos_por_especialidad(request):
    especialidad_id = request.GET.get('especialidad')
    medicos = Medico.objects.filter(especialidad_id=especialidad_id)
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer