# Generated by Django 4.1 on 2022-12-21 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_rename_services_service"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="experience",
            name="degree",
        ),
    ]
