# Generated by Django 3.0.6 on 2020-06-15 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiovan_app', '0005_motorista_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='logradouro',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='nome_endereco',
        ),
    ]