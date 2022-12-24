# Generated by Django 4.1 on 2022-12-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_review_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name="doctorimage",
            name="doctor",
        ),
        migrations.RemoveField(
            model_name="education",
            name="doctor",
        ),
        migrations.RemoveField(
            model_name="experience",
            name="doctor",
        ),
        migrations.RemoveField(
            model_name="service",
            name="doctor",
        ),
        migrations.RemoveField(
            model_name="specialization",
            name="doctor",
        ),
        migrations.DeleteModel(
            name="Award",
        ),
        migrations.DeleteModel(
            name="DoctorImage",
        ),
        migrations.DeleteModel(
            name="Education",
        ),
        migrations.DeleteModel(
            name="Experience",
        ),
        migrations.DeleteModel(
            name="Service",
        ),
        migrations.DeleteModel(
            name="Specialization",
        ),
    ]