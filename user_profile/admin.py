from django.contrib import admin
from user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "birth_date", "phone", "country")
    search_fields = ("country",)
