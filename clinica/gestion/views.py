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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Paciente, Medico, Cita , Horario

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

    # Crear perfil paciente
    Paciente.objects.create(usuario=user)

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
@permission_classes([IsAuthenticated])
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

@api_view(['GET'])
def medicos_por_especialidad(request):
    especialidad_id = request.GET.get('especialidad')
    medicos = Medico.objects.filter(especialidad_id=especialidad_id)
    data = [{"id": m.id, "nombres": m.nombres, "correo": m.correo} for m in medicos]
    return Response(data)

@api_view(['GET'])
def horarios_por_medico(request):
    medico_id = request.GET.get('medico')
    if not medico_id:
        return Response([], status=200)

    horarios = Horario.objects.filter(medico_id=medico_id, disponible=True).order_by('fecha', 'hora')
    data = [
        {
            "id": h.id,
            "fecha": h.fecha.isoformat(),  # YYYY-MM-DD
            "hora": h.hora.strftime('%H:%M')  # formato corto
        }
        for h in horarios
    ]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reservar_cita(request):
    user = request.user

    # Asegurarnos de que el usuario tenga perfil Paciente
    try:
        paciente = Paciente.objects.get(usuario=user)
    except Paciente.DoesNotExist:
        return Response({'error': 'Solo los pacientes pueden reservar citas.'},
                        status=status.HTTP_403_FORBIDDEN)

    medico_id = request.data.get('medico')
    fecha = request.data.get('fecha')
    hora = request.data.get('hora')

    if not (medico_id and fecha and hora):
        return Response({'error': 'Campos incompletos.'},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        medico = Medico.objects.get(pk=medico_id)
    except Medico.DoesNotExist:
        return Response({'error': 'Médico no encontrado.'},
                        status=status.HTTP_404_NOT_FOUND)

    # ¿Existe un horario marcado como disponible?
    horario = Horario.objects.filter(
        medico=medico,
        fecha=fecha,
        hora=hora,
        disponible=True
    ).first()

    if not horario:
        return Response({'error': 'Horario no disponible.'},
                        status=status.HTTP_400_BAD_REQUEST)

    # Crear cita
    cita = Cita.objects.create(
        paciente=paciente,
        medico=medico,
        fecha=fecha,
        hora=hora,
        estado='Pendiente'
    )

    # Marcar horario como ya usado
    horario.disponible = False
    horario.save()

    return Response({
        'message': 'Cita reservada con éxito.',
        'cita_id': cita.id,
        'fecha': fecha,
        'hora': hora,
        'medico': medico.nombres,
        'especialidad': medico.especialidad.nombre,
    }, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def perfil_paciente(request):
    """Devuelve (GET) o actualiza (PATCH) el perfil del paciente logueado."""
    try:
        paciente = Paciente.objects.select_related('usuario').get(usuario=request.user)
    except Paciente.DoesNotExist:
        return Response({'error': 'No es paciente.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        data = {
            'username': paciente.usuario.username,
            'email': paciente.usuario.email,
            'first_name': paciente.usuario.first_name,
            'last_name': paciente.usuario.last_name,
            'telefono': paciente.telefono,
        }
        return Response(data)

    # PATCH (actualizar campos opcionales)
    telefono = request.data.get('telefono')
    email = request.data.get('email')
    first = request.data.get('first_name')
    last = request.data.get('last_name')

    if telefono is not None:
        paciente.telefono = telefono
    if email is not None:
        paciente.usuario.email = email
    if first is not None:
        paciente.usuario.first_name = first
    if last is not None:
        paciente.usuario.last_name = last

    paciente.usuario.save()
    paciente.save()

    return Response({'message': 'Perfil actualizado.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def citas_paciente(request):
    """Devuelve todas las citas del paciente logueado (orden desc por fecha/hora)."""
    try:
        paciente = Paciente.objects.get(usuario=request.user)
    except Paciente.DoesNotExist:
        return Response({'error': 'No es paciente.'}, status=status.HTTP_403_FORBIDDEN)

    qs = (
        Cita.objects
        .filter(paciente=paciente)
        .select_related('medico', 'medico__especialidad')
        .order_by('-fecha', '-hora')
    )

    data = [
        {
            'id': c.id,
            'fecha': c.fecha.isoformat(),
            'hora': c.hora.strftime('%H:%M'),
            'estado': c.estado,
            'medico': c.medico.nombres,
            'especialidad': c.medico.especialidad.nombre,
        }
        for c in qs
    ]
    return Response(data)