# Generated by Django 3.0.8 on 2020-07-23 04:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='modified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
