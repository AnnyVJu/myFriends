# coding=utf-8
from django import forms
from meetingsite.models import Profile, Post


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Surname")
    email = forms.EmailField(label="Email", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self.add_error("password_confirm", "Wrong password.")
                return False
            elif len(self.cleaned_data['password']) < 5:
                self.add_error('password', "Too short.")
        return valid


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
