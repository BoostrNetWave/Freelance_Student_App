# Generated by Django 5.0.6 on 2024-07-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stages',
            field=models.TextField(default=''),
        ),
    ]
