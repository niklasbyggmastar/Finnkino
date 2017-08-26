# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rows', models.IntegerField(default=0)),
                ('number_of_cols', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('released', models.DateTimeField(verbose_name='date published')),
                ('genre', models.CharField(default='', max_length=15)),
                ('duration_mins', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=300)),
                ('poster', models.ImageField(default='', upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('released', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('stars', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=500)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=50)),
                ('show_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('auditorium', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movieapp.Auditorium')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('seat_row', models.IntegerField(default=0)),
                ('seat_col', models.IntegerField(default=0)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Show')),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Theatre'),
        ),
        migrations.AddField(
            model_name='auditorium',
            name='theatre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Theatre'),
        ),
    ]