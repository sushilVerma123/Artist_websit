# Generated by Django 4.1.13 on 2024-04-30 16:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_products_datetime'),
        ('message', '0003_project_list_customer_alter_contact_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 21, 47, 24, 244424)),
        ),
        migrations.AlterField(
            model_name='project_list',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 21, 47, 24, 244424)),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='store.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='store.customer')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]