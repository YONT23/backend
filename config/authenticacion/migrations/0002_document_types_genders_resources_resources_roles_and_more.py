# Generated by Django 4.1.7 on 2023-03-30 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Document_types',
                'verbose_name_plural': 'Document_types',
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Genders',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('path', models.CharField(max_length=256)),
                ('id_padre', models.IntegerField()),
                ('method', models.CharField(max_length=256)),
                ('icono', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Resources',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='Resources_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('resourcesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='authenticacion.resources')),
            ],
            options={
                'verbose_name': 'Resources_roles',
                'verbose_name_plural': 'Resources_roles',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('resources', models.ManyToManyField(related_name='roles_resources', through='authenticacion.Resources_roles', to='authenticacion.resources')),
            ],
            options={
                'verbose_name': 'Roles',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='User_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('rolesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='authenticacion.roles')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_roles',
                'verbose_name_plural': 'user_roles',
                'unique_together': {('userId', 'rolesId')},
            },
        ),
        migrations.AddField(
            model_name='roles',
            name='users',
            field=models.ManyToManyField(related_name='roles_user', through='authenticacion.User_roles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resources_roles',
            name='rolesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resouces_roles', to='authenticacion.roles'),
        ),
        migrations.AddField(
            model_name='resources',
            name='roles',
            field=models.ManyToManyField(related_name='resources_roles', through='authenticacion.Resources_roles', to='authenticacion.roles'),
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('surname', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('identification', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.BooleanField(default=True)),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_types', to='authenticacion.document_types')),
                ('gender_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gender_types', to='authenticacion.genders')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons',
                'verbose_name_plural': 'Persons',
                'unique_together': {('name', 'identification')},
            },
        ),
    ]