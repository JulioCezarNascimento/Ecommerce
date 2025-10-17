from django.urls import path
from . import views

app_name = 'perfil/'

urlpatterns = [
    path('', views.CriarPerfil.as_view(), name='CriarPerfil'),
    path('Atualizar/', views.AtualizarPerfil.as_view(), name='AtualizarPerfil'),
    path('Deletar/', views.DeletarPerfil.as_view(), name='DeletarPerfil'),
    path('Login/', views.Login.as_view(), name='Login'),
    path('Logout/', views.Logout.as_view(), name='Logout'),
]
