# Generated by Django 4.1 on 2022-12-22 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="header",
            new_name="title",
        ),
    ]
