from django import forms
from webapp.models import Status, Type

class DoingForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label='Summary')
    description = forms.CharField(max_length = 150, required=False, label='Description')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')