# Generated by Django 4.1 on 2022-12-21 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquire",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("number", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("program", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SiteDetail",
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
                ("logo", models.ImageField(upload_to="site/")),
                ("phone", models.CharField(max_length=13)),
                ("description", models.CharField(max_length=700)),
                ("email", models.EmailField(max_length=254)),
                ("descrition_header", models.CharField(max_length=70)),
                ("footer_description", models.CharField(max_length=400)),
                ("address", models.CharField(max_length=300)),
                ("insta_link", models.URLField()),
                ("linkedin_link", models.URLField()),
                ("fb_link", models.URLField()),
                ("twitter_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Speciality",
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
                (
                    "image",
                    models.ImageField(
                        default="speciality/specialities-01.png", upload_to="branch/"
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=40)),
                ("city", models.CharField(max_length=40)),
                ("state", models.CharField(max_length=40)),
                ("country", models.CharField(max_length=40)),
                ("price_low", models.IntegerField()),
                ("price_high", models.IntegerField()),
                ("picture", models.ImageField(upload_to="doctor/profile/")),
                (
                    "speciality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="doctors",
                        to="home.speciality",
                    ),
                ),
            ],
        ),
    ]
