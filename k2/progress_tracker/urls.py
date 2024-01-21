from django.urls import path
from . import views

app_name = "progress_tracker"

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("students/", views.student_list, name="student_list"),
    path(
        "update-progress-report/",
        views.update_progress_report,
        name="update_progress_report",
    ),
    path("progress_graph/", views.progress_graph, name="progress_graph"),
    path("marksheet/", views.marksheet, name="marksheet"),
    path("assignmnet_report/", views.assignmnet_report, name="assignmnet_report"),
    path("overall_progress/", views.overall_progress, name="overall_progress"),
]
