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
            'specialities':Speciality.objects.all()
        },
    )


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
    return render(request, "home/doctor/booking.html", {
        "doctor":Doctor.objects.get(slug=slug), 
        "detail":SiteDetail.objects.last()}
        )


def all_doctors(request):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = days[datetime.now().weekday()]
    return render(request, 'home/doctor/all-doctor-list.html', {
        "detail": SiteDetail.objects.last(),
        "specialities": Speciality.objects.all(),
        "hospitals":Hospital.objects.all().order_by("-id"),
        "doctors":Doctor.objects.raw(f"SELECT *, {day}!='closed' AS available FROM home_doctor ORDER BY id DESC")
        })
 
     
def all_hospitals(request):
    return render(request, "home/all-hospital-list.html", {
        "hospitals":Hospital.objects.all(),
        "detail": SiteDetail.objects.last(),
        'specialities':Speciality.objects.all()
    })


def filter_doctor(request):
    lst = [x for x in request.GET.keys()]
    if not len(lst):
        lst = [name["name"] for name in Speciality.objects.values("name")]
    print(lst)
    return render(
        request,
        "home/doctor/doctor-list.html",
        {
            "doctors": Doctor.objects.filter(speciality__name__in = lst),
            "detail": SiteDetail.objects.last(),
            'specialities':Speciality.objects.all(),
            'searching_doctors':True,
        },
    )


def filter_hospital(request):
    lst = [x for x in request.GET.keys()]
    if not len(lst):
        lst = [name["name"] for name in Speciality.objects.values("name")]
    print(lst, Hospital.objects.filter(speciality__name__in = lst),)
    return render(
        request,
        "home/all-hospital-list.html",
        {
            "hospitals":Hospital.objects.filter(speciality__name__in = lst),
            "detail": SiteDetail.objects.last(),
            'specialities':Speciality.objects.all(),
            'searching_hospitals':True,
        },
    )



