from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.RegistroUsuario.as_view(), name='registro_usuario'),
    path('login/', views.InicioSesion.as_view(), name='login'),
    path('logout/', views.CerrarSesion.as_view(), name='logout'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
]
