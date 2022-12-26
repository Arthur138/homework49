from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}


    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if last_name or first_name:
            pass
        else:
            raise ValidationError('Fill out First name or Second name ')