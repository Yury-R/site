from django.contrib import admin
from django.contrib.admin import helpers

from user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "birth_date", "phone", "country")
    search_fields = ("user",)
    list_editable = ("birth_date", "country", "phone")
    list_filter = ("country", )
    action_form = helpers.ActionForm
