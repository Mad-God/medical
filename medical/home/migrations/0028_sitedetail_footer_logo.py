# Generated by Django 4.1 on 2022-12-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0027_doctorimage_doctorservices_delete_enquire_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitedetail",
            name="footer_logo",
            field=models.ImageField(blank=True, null=True, upload_to="site/"),
        ),
    ]
