from django.urls import path, include
from home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("doctor-profile/<int:pk>", views.doctor_detail, name="doctor-profile"),
    path("doctor-list", views.doctor_list, name="doctor-list"),
    path("booking/<int:pk>", views.doctor_booking, name="doctor-booking"),
]
