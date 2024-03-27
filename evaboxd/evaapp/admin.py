from django.contrib import admin
from .models import Show, Episode


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class ShowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["show_title", "show_date"]})
    ]
    inlines = [EpisodeInline]


admin.site.register(Show, ShowAdmin)
