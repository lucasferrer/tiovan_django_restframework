# Generated by Django 3.0.6 on 2020-06-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiovan_app', '0007_auto_20200615_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='latitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='longitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
