# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from api.models import CustomUser  # Asegúrate de importar tu modelo de usuario si es necesario

# class Command(BaseCommand):
#     help = 'Crea roles para depósitos globales y proveedores y asigna permisos'

#     def handle(self, *args, **kwargs):
#         # Crear grupo para depósitos globales
#         depositos_globales_group, created = Group.objects.get_or_create(name='Depósitos Globales')

#         # Crear grupo para depósitos proveedores
#         depositos_proveedores_group, created = Group.objects.get_or_create(name='Depósitos Proveedores')

#         # Definir permisos específicos
#         permisos_globales = [
#             'add_pedido',
#             # Añade otros permisos específicos si es necesario
#         ]
        
#         permisos_proveedores = [
#             'add_reserva',
#             # Añade otros permisos específicos si es necesario
#         ]

#         # Asignar permisos al grupo de depósitos globales
#         for permiso_codename in permisos_globales:
#             permiso = Permission.objects.get(codename=permiso_codename)
#             depositos_globales_group.permissions.add(permiso)

#         # Asignar permisos al grupo de depósitos proveedores
#         for permiso_codename in permisos_proveedores:
#             permiso = Permission.objects.get(codename=permiso_codename)
#             depositos_proveedores_group.permissions.add(permiso)

#         self.stdout.write(self.style.SUCCESS('Roles creados y permisos asignados correctamente.'))
