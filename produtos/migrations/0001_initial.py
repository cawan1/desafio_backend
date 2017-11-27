# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 03:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='imagens')),
                ('valor', models.FloatField()),
                ('fator', models.CharField(choices=[('A', 'FATOR A'), ('B', 'FATOR B'), ('C', 'FATOR C')], max_length=1)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
