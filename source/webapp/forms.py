from django import forms
from webapp.models import Status, Type

class DoingForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label='Название')
    description = forms.CharField(max_length = 150, required=False, label='Описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())