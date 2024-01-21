# progress_tracker/forms.py

from django import forms


class ProgressReportForm(forms.Form):
    progress_report_id = forms.IntegerField(widget=forms.HiddenInput())
    marks = forms.IntegerField()
    comments = forms.CharField(widget=forms.Textarea)
