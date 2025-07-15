from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.response import Response
from .models import Especialidad, Medico
from .serializers import EspecialidadSerializer, MedicoSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# Create your views here.
def angular_app(request):
    return render(request, 'index.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'error': 'Todos los campos son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)

    # 🔁 Generar URL completa a la vista de login
    login_url = request.build_absolute_uri(reverse('api_login'))

    # ✅ Envío de correo de confirmación
    try:
        send_mail(
            subject='Registro exitoso en Citas Médicas',
            message=f'Hola {username}, tu registro fue completado exitosamente.',
            from_email='notificaciones@citasmedicas.com',  # Usa el mismo que pusiste en settings.py
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        return Response({'error': f'Usuario creado, pero hubo un error al enviar el correo: {str(e)}'}, status=201)

    return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
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
