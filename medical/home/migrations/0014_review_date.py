# Generated by Django 4.1 on 2022-12-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_rename_header_review_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]