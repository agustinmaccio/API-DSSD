from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.shortcuts import render, redirect

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Autenticar al usuario usando el modelo de usuario por defecto
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generar tokens JWT
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(access),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


def home(request):
    # Si el usuario no es un depósito, simplemente renderizar la página
    return render(request, 'home.html')


def CRC(request):
    # Lógica para la página de inicio de sesión
    return render(request, 'CRC.html')


def carga_pedidos(request):
    return render(request, 'carga_pedidos.html')


import json
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone 
import pprint

def carga_pedidos(request):
    if request.method == 'POST':
        # Procesar el JSON recibido
        try:
            # Cargar el JSON desde el body de la petición
            data = json.loads(request.body)

            # Obtener cliente_id, por ejemplo, del usuario autenticado
            id_cliente = request.user.id if request.user.is_authenticated else 'test_1'

            # Obtener la fecha actual
            date_now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

            # Agregar el cliente_id y la fecha al dict de respuesta
            response_data = {
                'data': data,
                'cliente_id': id_cliente,
                'fecha': date_now
            }

            ### TODO guarda en API
            pprint.pprint(response_data)

            # Aquí puedes hacer lo que necesites con los datos recibidos
            return JsonResponse({'success': True, 'data': data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    return render(request, 'carga_pedidos.html')