from django.contrib import admin
from django.contrib.admin import helpers

from home.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author")
    search_fields = ("title",)
    search_fields = ("title",)
    list_filter = ("content", )
    action_form = helpers.ActionForm
