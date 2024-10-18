# Generated by Django 5.0.6 on 2024-09-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_supportinfo_consultingmessage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportinfo',
            old_name='image',
            new_name='support_image',
        ),
        migrations.RemoveField(
            model_name='consultingmessage',
            name='image',
        ),
        migrations.AddField(
            model_name='supportinfo',
            name='contatus_image',
            field=models.ImageField(blank=True, help_text='Upload a contatus related image', null=True, upload_to='contatus_images/'),
        ),
    ]
