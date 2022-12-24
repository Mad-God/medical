from django.contrib import admin
from home.models import Speciality, SiteDetail, Doctor, Review, Hospital, Booking

# Register your models here.

admin.site.register(Doctor)
admin.site.register(SiteDetail)
admin.site.register(Speciality)
admin.site.register(Review)
admin.site.register(Hospital)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "doctor",
        "phone",
        "email",
        "time",
        "date",
    )
