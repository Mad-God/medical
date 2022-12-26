from django.urls import path, include
from home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("doctor-profile/<slug>", views.doctor_detail, name="doctor-profile"),
    path("all-doctor-list", views.all_doctors, name="all-doctor-list"),
    path("all-hospital-list", views.all_hospitals, name="all-hospital-list"),
    path("doctor-list", views.doctor_list, name="doctor-list"),
    path("filter-doctor", views.filter_doctor, name="filter-doctor"),
    path("filter-hospital", views.filter_hospital, name="filter-hospital"),
    path("booking/<slug>", views.doctor_booking, name="doctor-booking"),
]
