from django import forms
from webapp.models import Status, Type
from django.forms import widgets

class DoingForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length = 2000, required=False, label='Description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')