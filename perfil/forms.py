from django import forms
from django.contrib.auth.models import User
from . import models
from django.apps import apps

class PerfilForm(forms.ModelForm):
       class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ['user']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        
        


 