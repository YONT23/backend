# Generated by Django 4.1.7 on 2023-03-17 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0003_usuario_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personas',
            name='correo_electronico',
        ),
    ]