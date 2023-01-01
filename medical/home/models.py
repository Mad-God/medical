from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    price_low = models.IntegerField()
    price_high = models.IntegerField()
    picture = models.ImageField(upload_to="doctor/profile/")
    qualification = models.CharField(max_length=40, null=True, blank=True)
    overview = models.CharField(max_length=700, blank=True, null=True)
    hospital = models.ForeignKey(
        "Hospital",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor",
    )
    speciality = models.ForeignKey(
        "Speciality",
        on_delete=models.SET_NULL,
        related_name="doctors",
        null=True,
        blank=True,
    )
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)
    message_link = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    video_link = models.CharField(max_length=30)
    monday = models.CharField(max_length=30, default="closed")
    tuesday = models.CharField(max_length=30, default="closed")
    wednesday = models.CharField(max_length=30, default="closed")
    thursday = models.CharField(max_length=30, default="closed")
    friday = models.CharField(max_length=30, default="closed")
    saturday = models.CharField(max_length=30, default="closed")
    sunday = models.CharField(max_length=30, default="closed")

    def __str__(self) -> str:
        return self.name


class SiteDetail(models.Model):
    logo = models.ImageField(upload_to="site/")
    footer_logo = models.ImageField(upload_to="site/", blank=True, null=True)
    phone = models.CharField(max_length=13)
    description = models.CharField(max_length=700)
    email = models.EmailField()
    description_header = models.CharField(max_length=70)
    footer_description = models.CharField(max_length=400)
    address = models.CharField(max_length=300)
    insta_link = models.URLField()
    linkedin_link = models.URLField()
    fb_link = models.URLField()
    twitter_link = models.URLField()


class Speciality(models.Model):
    image = models.ImageField(
        upload_to="branch/", default="speciality/specialities-01.png"
    )
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)

    def __str__(self):
        return self.name


class Customer(User):
    name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    phone = models.CharField(max_length=13)
    picture = models.ImageField(upload_to="customer/profile")


class Review(models.Model):
    title = models.CharField(max_length=100)
    review = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    doctor = models.ForeignKey(
        "Doctor", on_delete=models.CASCADE, related_name="review"
    )
    date = models.DateField(auto_now_add=True, blank=True, null=True)


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = RichTextField()
    opening_timing = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    speciality = models.ForeignKey(
        "Speciality",
        related_name="hospital",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    picture = models.ImageField(upload_to="hospital", null=True, blank=True)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)


class Booking(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(
        "Doctor", on_delete=models.CASCADE, related_name="booking"
    )
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=30)


class DoctorImage(models.Model):
    image = models.ImageField(upload_to="doctor/images")
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="image")


class DoctorServices(models.Model):
    name = models.CharField(max_length=20)
    doctor = models.ForeignKey(
        "Doctor", on_delete=models.CASCADE, related_name="service"
    )


class ContactRequest(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    message = models.CharField(max_length=130)
