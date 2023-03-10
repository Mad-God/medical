# Generated by Django 4.1 on 2022-12-26 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_hospital_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="hospital",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="doctor",
                to="home.hospital",
            ),
        ),
    ]
