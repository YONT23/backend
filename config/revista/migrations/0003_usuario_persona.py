# Generated by Django 4.1.7 on 2023-03-17 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0002_tipousuario_alter_personas_options_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='revista.personas'),
            preserve_default=False,
        ),
    ]
