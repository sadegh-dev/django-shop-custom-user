from django import forms
from django.forms import fields
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(lable='password', widget=forms.PasswordInput)
    password2 = forms.CharField(lable='confirm password', widget=forms.PasswordInput)

    class Meta :
        model = User
        fields = ('email','full_name')

        def clean_password2(self):
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 and password2 and password1 != password2 :
                raise forms.ValidationError('password is not match')
            return password2
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self, cleaned_data['password1'])
            if commit :
                user.save()
            return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta :
        model = User
        fields = ('email','password','full_name')
    
    def clean_password(self):
        return self.initial['pasword']
