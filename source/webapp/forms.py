from django import forms
from webapp.models import Status, Type , Doings
from django.forms import widgets , ValidationError

from webapp.models import Projects


class DoingForm(forms.ModelForm):
    class Meta:
        model = Doings
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'description':widgets.Textarea, 'type':widgets.CheckboxSelectMultiple}

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 3:
            self.add_error('summary', ValidationError('*Введите больше 3 символов'))
        return summary

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError('Описание не должно совпадать с названием')
        return cleaned_data



class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {'start_date':widgets.SelectDateWidget, 'end_date':widgets.SelectDateWidget}

class UserInProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['users']
        widgets = {'users': widgets.CheckboxSelectMultiple}