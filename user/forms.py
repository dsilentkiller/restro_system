from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from django import forms

from user.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data('email')
        qs = User.objects.filter(email='email')
        if qs.exists():
            raise forms.ValidationError('Email is taken')
        return email

    def clean(self):
        'verify both passwords match'
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 is not None and password1 != password2:
            self.add_error('password2', 'your passwords must match')
            return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_password(self):
        return self.initial['password1']
