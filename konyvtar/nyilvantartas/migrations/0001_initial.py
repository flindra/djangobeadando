# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('birth_year', models.IntegerField()),
                ('birth_place', models.CharField(max_length=60)),
                ('death_year', models.IntegerField()),
                ('death_place', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('publisher', models.CharField(max_length=60)),
                ('year', models.DateTimeField(verbose_name='date published')),
                ('btype', models.CharField(choices=[('1m', '1 hónapos kölcsönzés'), ('1w', '1 hetes kölcsönzés'), ('0w', 'nem kölcsönözhető')], default='1m', max_length=2)),
                ('author', models.ManyToManyField(to='nyilvantartas.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lending_date', models.DateTimeField(verbose_name='date lended')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyilvantartas.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('birth_year', models.IntegerField()),
                ('birth_place', models.CharField(max_length=60)),
                ('work_place', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='lending',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyilvantartas.User'),
        ),
    ]
