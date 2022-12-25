from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from django.db.models import Q
from django.utils.timezone import datetime
# Create your views here.


def home(request):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = days[datetime.now().weekday()]
    return render(
        request,
        "home/index.html",
        {
            "detail": SiteDetail.objects.last(),
            "specialities": Speciality.objects.all(),
            "hospitals":Hospital.objects.all().order_by("-id"),
            "doctors": Doctor.objects.raw(f"SELECT *, {day}!='closed' AS available FROM home_doctor ORDER BY id DESC")
        },
    )


def doctor_detail(request, slug):
    if request.method == "POST":
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken", None)
        data = {k: v[0] for k, v in data.items()}
        Review.objects.create(doctor=Doctor.objects.get(slug=slug), **data)
        messages.success(request, "Review Added successfully !")
    return render(
        request,
        "home/doctor/doctor-profile.html",
        {
            "doctor": Doctor.objects.get(slug=slug),
            "detail": SiteDetail.objects.last(),
            "reviews": Review.objects.filter(doctor__slug=slug).order_by("-id"),
        },
    )


def doctor_list(request):
    data = {k: v for k, v in request.GET.items()}
    return render(
        request,
        "home/doctor/doctor-list.html",
        {
            "doctors": Doctor.objects.filter(
                Q(city__icontains=data.get("location",""))
                | Q(state__icontains=data.get("location",""))
                | Q(country__icontains=data.get("location",""))
            ).filter(
                Q(name__icontains=data.get("keyword",""))
                | Q(hospital__name__icontains=data.get("keyword",""))
                | Q(speciality__name__icontains=data.get("keyword",""))
            ),
            
            "detail": SiteDetail.objects.last(),
        },
    )
'''
Doctor.objects.raw(f
"SELECT *, {day}!='closed' AS available FROM home_doctor WHERE 
(city LIKE '%{location}%' OR state LIKE '%{location}%' OR country LIKE '%{location%}') 
AND (city LIKE '%{keyword}%' OR state LIKE '%{keyword}%' OR country LIKE '%{keyword%}')
'''

def doctor_booking(request, slug):
    if request.method == "POST":
        # breakpoint()
        data = request.POST
        data._mutable = True
        data.pop("csrfmiddlewaretoken")
        data = {k:v for k,v in data.items()}
        data["doctor"] = Doctor.objects.get(slug=slug)
        Booking.objects.create(**data)
        messages.success(request, "Appointment Booked successfully")
        return redirect("home:home")
    return render(request, "home/doctor/booking.html", {"doctor":Doctor.objects.get(slug=slug), "detail":SiteDetail.objects.last()})




def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        data = request.POST
        enq = Enquire(
            name=data["name"],
            email=data["email"],
            number=data["number"],
        )
        messages.success(request, "Successfully Submit")
        enq.save()

    return render(request, "home/contact.html", {"doctor": Doctor.objects.first()})
