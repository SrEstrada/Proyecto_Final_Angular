from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
def angular_app(request):
    return render(request, 'index.html')

@api_view(['POST'])
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