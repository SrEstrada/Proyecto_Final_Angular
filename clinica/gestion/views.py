from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Especialidad, Medico
from .serializers import EspecialidadSerializer, MedicoSerializer
from rest_framework import viewsets
from rest_framework import status



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

@api_view(['GET'])
def listar_especialidades(request):
    especialidades = Especialidad.objects.all()
    serializer = EspecialidadSerializer(especialidades, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_especialidad(request):
    serializer = EspecialidadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def editar_especialidad(request, pk):
    try:
        especialidad = Especialidad.objects.get(pk=pk)
    except Especialidad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EspecialidadSerializer(especialidad, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_especialidad(request, pk):
    try:
        especialidad = Especialidad.objects.get(pk=pk)
        especialidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Especialidad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)