# Generated by Django 3.0.2 on 2020-01-27 00:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="camera",
            old_name="rover_id",
            new_name="rover",
        ),
        migrations.RenameField(
            model_name="photo",
            old_name="camera_id",
            new_name="camera",
        ),
    ]
