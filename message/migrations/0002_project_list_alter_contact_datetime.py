# Generated by Django 4.2.3 on 2023-12-09 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=10000)),
                ('checkpoint', models.BooleanField(default=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 12, 9, 19, 16, 24, 631215))),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 19, 16, 24, 631215)),
        ),
    ]
