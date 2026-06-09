from django import forms
from django.contrib.auth.models import User
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ['usuario']

class UserForm(forms.ModelForm):
    confirmed_password = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        