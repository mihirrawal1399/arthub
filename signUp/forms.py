from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # address = forms.CharField(max_length=500)
    # mobile_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$',
                                 message="Phone number must be entered in the format:"
                                         " '+911234567890'. Up to 10 digits allowed.")
    mobile_no = forms.CharField(validators=[phone_regex], max_length=17, initial='+91')  # validators should be a list

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_no', 'password1', 'password2')
