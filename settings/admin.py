from django.contrib import admin

from settings.models import Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "value")
    list_editable = ("value",)
    list_filter = ("category",)
    search_fields = ("name",)
