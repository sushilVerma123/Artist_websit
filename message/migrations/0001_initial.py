# Generated by Django 4.2.3 on 2023-12-09 12:03

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user_messages', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 12, 9, 17, 33, 4, 378291))),
            ],
        ),
        migrations.CreateModel(
            name='Messagee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciver_id', models.IntegerField()),
                ('sender_id', models.IntegerField()),
                ('messages', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, default='profile/person_icon.jpg', null=True, upload_to='profile')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Specified', 'Not Specified')], default='Not Specified', max_length=20)),
                ('mobile', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=500, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]