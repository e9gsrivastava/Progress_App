from django.contrib import admin
from .models import Trainee, ProgressReport


class TraineeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "name")
    search_fields = ("username", "name")


class ProgressReportAdmin(admin.ModelAdmin):
    list_display = (
        "trainee",
        "week_number",
        "attendance",
        "assignment",
        "marks",
        "comments",
    )
    list_filter = ("week_number",)
    search_fields = ("trainee__username", "trainee__name")


admin.site.register(Trainee, TraineeAdmin)
admin.site.register(ProgressReport, ProgressReportAdmin)
