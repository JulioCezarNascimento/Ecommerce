from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

from . import models
from . import forms

class BasePerfil(View):
    template_name = 'perfil/criar.html'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contexto = None
        self.renderizar = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.contexto = {
            'userform': forms.UserForm(
                data=self.request.POST or None
            ),
            'perfilform': forms.ProfileForm(
                data=self.request.POST or None,
            )
        }
        
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
    def get(self, *args, **kwargs):
        return self.renderizar

class CriarPerfil(BasePerfil):
    pass
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
