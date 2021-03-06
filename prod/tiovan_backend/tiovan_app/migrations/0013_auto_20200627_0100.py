# Generated by Django 3.0.6 on 2020-06-27 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiovan_app', '0012_auto_20200625_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicoes',
            name='motorista',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tiovan_app.Motorista'),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='endereco',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='tiovan_app.Endereco'),
        ),
    ]
