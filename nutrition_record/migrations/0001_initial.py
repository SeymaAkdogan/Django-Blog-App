# Generated by Django 3.2.9 on 2022-06-10 11:01

import datetime
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
            name='Nutrition_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('repast', models.JSONField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 10, 14, 1, 50, 796622))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 10, 14, 1, 50, 796622))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
