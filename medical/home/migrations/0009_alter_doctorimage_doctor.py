# Generated by Django 4.1 on 2022-12-21 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_rename_qualification_doctor_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorimage",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctorimage",
                to="home.doctor",
            ),
        ),
    ]
