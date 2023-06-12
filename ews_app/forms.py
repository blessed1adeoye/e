from django import forms
from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    first_name = forms.CharField(label="", max_length=111, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(label="", max_length=111, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 character or fewer, Letters, digits and @/./+/-/_ only.</small> </span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same Password as before, for verification </small></span>'


# PROFILE EXTRAS FORM Welcome to EWS  Elite Whales is a community-driven token on Binance Smart Chain Created by blockchain experts and crypto enthusiasts. They aim to onboard web2 businesses and users into web3 with cutting-edge technology and innovations for long-term investment safety. EWS is an educational-meme token, AI driven with core objectives of giving back to the community through skills acquisition, blockchain awareness, job creation, charity and quality education.

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")

    class Meta:
        model = Profile
        fields = ('profile_image',)


class HomeWelcomeForm(ModelForm):
    class Meta:
        model = Welcome
        fields = ('__all__')

        labels = {
            'wel_title': 'TITLE',
            'wel_speech': 'SPEECH',
        }
        widgets = {
            'wel_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title Here'}),
            'wel_speech': forms.Textarea(attrs={'class': 'form-control', 'height': '100px'})
        }


class INVESTMENTForm(ModelForm):
    class Meta:
        model = HomeSecondSection
        fields = '__all__'

        labels = {
            'title': 'INVESTMENT TITLE',
            'speech': ' INVESTMENT SPEECH',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title Here'}),
            'speech': forms.Textarea(attrs={'class': 'form-control', 'height': '100px'})
        }


class HomeThirdForm(ModelForm):
    class Meta:
        model = HomeThird
        fields = '__all__'

        # labels = {
        #     'title': 'INVESTMENT TITLE',
        #     'speech': ' INVESTMENT SPEECH',
        # }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title Here'}),
        #     'speech': forms.Textarea(attrs={'class': 'form-control', 'height': '100px'})
        # }
        #
