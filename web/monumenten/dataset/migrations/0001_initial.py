# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-23 14:37
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('beschrijving', models.TextField(null=True)),
                ('monumentnummer', models.IntegerField(null=True)),
                ('naam', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('aanwijzingsdatum', models.DateField(null=True)),
                ('architect', models.CharField(max_length=128, null=True)),
                ('beperking', models.IntegerField(null=True)),
                ('beschrijving', models.TextField(null=True)),
                ('coordinaten', django.contrib.gis.db.models.fields.PointField(null=True, srid=28992)),
                ('afbeelding', models.CharField(max_length=36, null=True)),
                ('functie', models.CharField(max_length=128, null=True)),
                ('geometrie', django.contrib.gis.db.models.fields.GeometryCollectionField(null=True, srid=28992)),
                ('in_onderzoek', models.CharField(max_length=3, null=True)),
                ('monumentnummer', models.IntegerField(null=True)),
                ('naam', models.CharField(max_length=255, null=True)),
                ('opdrachtgever', models.CharField(max_length=128, null=True)),
                ('pand_sleutel', models.BigIntegerField(default=0)),
                ('periode_start', models.IntegerField(null=True)),
                ('periode_eind', models.IntegerField(null=True)),
                ('redengevende_omschrijving', models.TextField(null=True)),
                ('status', models.CharField(max_length=128, null=True)),
                ('type', models.CharField(max_length=128, null=True)),
                ('complex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monumenten', to='dataset.Complex')),
            ],
        ),
        migrations.CreateModel(
            name='Situering',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('betreft', models.IntegerField(null=True)),
                ('situering_nummeraanduiding', models.CharField(max_length=128, null=True)),
                ('eerste_situering', models.CharField(max_length=3, null=True)),
                ('huisletter', models.CharField(max_length=1, null=True)),
                ('huisnummer', models.IntegerField(null=True)),
                ('nummeraanduiding', models.CharField(max_length=255, null=True)),
                ('postcode', models.CharField(max_length=6, null=True)),
                ('straat', models.CharField(max_length=80, null=True)),
                ('toevoeging', models.CharField(max_length=4, null=True)),
            ],
        ),
    ]
