# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-12-06 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import estante.models.pessoa


class Migration(migrations.Migration):

    dependencies = [
        ('estante', '0002_cadastralivro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[estante.models.pessoa.validate_cpf]),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.IntegerField(max_length=11, validators=[estante.models.pessoa.validate_phone]),
        ),
    ]
