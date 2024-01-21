from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Trainee, ProgressReport
from .forms import ProgressReportForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("progress_tracker:student_list")
    else:
        form = AuthenticationForm()
    return render(request, "progress_tracker/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("progress_tracker:login")


@login_required
def student_list(request):
    progress_reports = ProgressReport.objects.select_related("trainee").all()
    return render(
        request,
        "progress_tracker/student_list.html",
        {"progress_reports": progress_reports},
    )


@login_required
def update_progress_report(request):
    if request.method == "POST":
        form = ProgressReportForm(request.POST)
        if form.is_valid():
            progress_report_id = form.cleaned_data["progress_report_id"]
            marks = form.cleaned_data["marks"]
            comments = form.cleaned_data["comments"]

            progress_report = get_object_or_404(ProgressReport, id=progress_report_id)

            progress_report.marks = marks
            progress_report.comments = comments
            progress_report.save()

            return redirect("progress_tracker:student_list")
    else:
        form = ProgressReportForm()

    return render(
        request, "progress_tracker/update_progress_report.html", {"form": form}
    )


@login_required
def progress_graph(request):
    all_trainees = Trainee.objects.all()
    attendance_data = {}
    for trainee in all_trainees:
        progress_reports = ProgressReport.objects.filter(trainee=trainee)
        percentages = [report.attendance / 100.0 for report in progress_reports]
        attendance_data[trainee.username] = percentages

    return render(
        request,
        "progress_tracker/progress_graph.html",
        {"attendance_data": attendance_data},
    )


@login_required
def progress_graph(request):
    all_trainees = Trainee.objects.all()
    attendance_data = {}
    for trainee in all_trainees:
        progress_reports = ProgressReport.objects.filter(trainee=trainee)
        percentages = [report.attendance / 100.0 for report in progress_reports]
        attendance_data[trainee.username] = percentages

    return render(
        request,
        "progress_tracker/progress_graph.html",
        {"attendance_data": attendance_data},
    )


@login_required
def marksheet(request):
    all_trainees = Trainee.objects.all()
    mark_data = {}
    for trainee in all_trainees:
        progress_reports = ProgressReport.objects.filter(trainee=trainee)
        marks = [report.marks / 100.0 for report in progress_reports]
        mark_data[trainee.username] = marks

    return render(request, "progress_tracker/marksheet.html", {"mark_data": mark_data})


@login_required
def assignmnet_report(request):
    all_trainees = Trainee.objects.all()
    assignment_data = {}
    for trainee in all_trainees:
        progress_reports = ProgressReport.objects.filter(trainee=trainee)
        assignments = [report.assignment / 100.0 for report in progress_reports]
        assignment_data[trainee.username] = assignments

    return render(
        request,
        "progress_tracker/assignmnet_report.html",
        {"assignment_data": assignment_data},
    )



@login_required
def overall_progress(request):
    all_trainees = Trainee.objects.all()
    overall_data = {}

    for trainee in all_trainees:
        progress_reports = ProgressReport.objects.filter(trainee=trainee)

        attendance_percentage = (
            progress_reports.aggregate(average=Avg("attendance"))["average"] / 100.0
            if progress_reports
            else 0
        )
        marks_percentage = (
            progress_reports.aggregate(average=Avg("marks"))["average"] / 100.0
            if progress_reports
            else 0
        )
        assignment_percentage = (
            progress_reports.aggregate(average=Avg("assignment"))["average"] / 100.0
            if progress_reports
            else 0
        )

        overall_average = (
            attendance_percentage + marks_percentage + assignment_percentage
        ) / 3

        overall_data[trainee.username] = overall_average

    return render(
        request,
        "progress_tracker/overall_progress.html",
        {"overall_data": overall_data},
    )
