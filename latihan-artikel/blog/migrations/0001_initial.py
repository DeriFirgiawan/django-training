# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-05 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
                ('penulis', models.CharField(max_length=100)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
    ]