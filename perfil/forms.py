from platform import node
from django import forms
from django.contrib.auth.models import User
from . import models
from django.apps import apps

class ProfileForm(forms.ModelForm):
       class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ['user']
        
class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )
    confirmed_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação de Senha'
    )
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.usuario = usuario
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'confirmed_password','email')
        
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}
        
        usuario_data = cleaned.get('username')
        password_data = cleaned.get('password')
        confirmed_password_data = cleaned.get('confirmed_password')
        email_data = cleaned.get('email')
        
        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()
        
        error_msg_user_exists = 'Usuário já cadastrado.'
        error_msg_email_exists = 'E-mail já cadastrado.'
        error_msg_password_mismatch = 'As senhas não coincidem.'
        
        if self.usuario:
            if usuario_db and usuario_db.pk != self.usuario.pk:
                validation_error_msgs['username'] = error_msg_user_exists
            
            if email_db and email_db.pk != self.usuario.pk:
                validation_error_msgs['email'] = error_msg_email_exists
            
            if password_data or confirmed_password_data:
                if password_data != confirmed_password_data:
                    validation_error_msgs['password'] = error_msg_password_mismatch
        else:
            validation_error_msgs
        
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
        


 