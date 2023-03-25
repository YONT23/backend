# Generated by Django 4.1.7 on 2023-03-17 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='personas',
            options={},
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='revista.tipousuario')),
            ],
        ),
    ]
