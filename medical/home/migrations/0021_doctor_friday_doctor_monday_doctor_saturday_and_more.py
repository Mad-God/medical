# Generated by Django 4.1 on 2022-12-23 17:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_doctor_video_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="friday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="monday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="saturday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="sunday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="thursday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="tuesday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="wednesday",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="hospital",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
