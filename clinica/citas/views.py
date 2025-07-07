from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def angular_app(request):
    return render(request, 'index.html')

@csrf_exempt
@api_view(['POST'])
def crear_cita(request):
    try:
        especialidad = request.data.get('especialidad')
        fecha = request.data.get('fecha')
        hora = request.data.get('hora')

        print(f"Cita recibida: {especialidad}, {fecha}, {hora}")

        return Response({"mensaje": "Cita creada con éxito"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("Error al crear cita:", e)
        return Response({"error": "Error al crear cita"}, status=status.HTTP_400_BAD_REQUEST)

