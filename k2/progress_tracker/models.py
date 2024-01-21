# progress_report/models.py

from django.db import models


class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)


class ProgressReport(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    attendance = models.PositiveIntegerField()
    assignment = models.PositiveIntegerField()
    marks = models.PositiveIntegerField()
    comments = models.TextField()
