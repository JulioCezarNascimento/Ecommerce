# Generated by Django 5.2.4 on 2025-07-16 21:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero',
            field=models.CharField(help_text='Número da residência', max_length=5, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
