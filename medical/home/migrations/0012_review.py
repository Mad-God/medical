# Generated by Django 4.1 on 2022-12-22 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("header", models.CharField(max_length=100)),
                ("review", models.CharField(max_length=300)),
                ("name", models.CharField(max_length=50)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review",
                        to="home.doctor",
                    ),
                ),
            ],
        ),
    ]