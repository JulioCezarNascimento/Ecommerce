from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class CriarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de criação de perfil")

class AtualizarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de atualização de perfil")

class DeletarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de deletar perfil")

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de login")

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de logout")
