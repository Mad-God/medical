# Generated by Django 4.1 on 2022-12-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0018_doctor_opening_timing"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="message_link",
            field=models.CharField(default="google.com", max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctor",
            name="phone",
            field=models.CharField(default="12312312312", max_length=13),
            preserve_default=False,
        ),
    ]