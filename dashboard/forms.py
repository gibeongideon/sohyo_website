


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Feedback

User = get_user_model()



class SignUpForm(UserCreationForm):
    """Prepares help texts, class and placeholder attributes.

    Define methods to increase and decrese token_count amount,
    betting and check if bet is possible.
    """

    # username = forms.CharField(
    #     max_length=50, required=True,
    #     label='',
    #     # help_text='E.g   07200200200 or 01200200200',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'e.g Darius'
    #     }))

    # first_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your first name...'
    #     }))

    # last_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your last name...'
    #     }))

    # phone_number = forms.CharField(max_length=150, required=True,
    #     label='',
    #     help_text='E.g   07200200200 or 01200200200',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your phone Number...'
    #     }))

    # email = forms.EmailField(
    #     max_length=254, required=True,
    #     label='',
    #     #  help_text='Required.Enter valid email.Required wen if you forot password.',
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter valid email...'
    #     }))

    # user_type = forms.CharField(
    #     max_length=150,
    #     label='',
    #     help_text='If others fill',
    #     widget=forms.TextInput(attrs={
    #         # 'class': 'form-control',
    #         'placeholder': 'user_type'
    #     }))
    # others = forms.CharField(
    #     required=False,
    #     max_length=150,
    #     label='',
    #     help_text='If others fill',
    #     widget=forms.TextInput(attrs={
    #         # 'class': 'form-control',
    #         'placeholder': 'If others specify'
    #     }))

    password1 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-control',
            'placeholder': 'Password...'
        }))

    password2 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-control',
            'placeholder': 'Confirm password...'
        }))

    class Meta:
        model = User
        fields = (
            'username','first_name','last_name', 'email','phone_number',
            'member_type','others', 'password1', 'password2')

   


class FeedBackForm(forms.ModelForm):
        # first_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your first name...'
    #     }))

    # last_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your last name...'
    #     }))

    # phone_number = forms.CharField(max_length=150, required=True,
    #     label='',
    #     help_text='E.g   07200200200 or 01200200200',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Your phone Number...'
    #     }))

    # email = forms.EmailField(
    #     max_length=254, required=True,
    #     label='',
    #     #  help_text='Required.Enter valid email.Required wen if you forot password.',
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter valid email...'
    #     }))

    
    class Meta:
        model = Feedback
        fields = ('message', 'full_name', 'email', 'subject')
