# Generated by Django 4.2.7 on 2024-09-19 04:17

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_merge_20240919_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=home.models.file_directory),
        ),
    ]
