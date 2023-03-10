# Generated by Django 4.1 on 2022-12-22 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_doctor_hospital_hospital_opening_timing_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="hospital",
            name="speciality",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="hospital",
                to="home.speciality",
            ),
        ),
    ]
