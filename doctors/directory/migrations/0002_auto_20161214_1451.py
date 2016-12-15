# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(to='directory.Specialty'),
        ),
    ]