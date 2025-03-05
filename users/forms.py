from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }),
        label="Password"
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Add placeholders for all input fields
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email Address'
        })
    
    def clean_password(self):
        """
        Validates that the password meets basic security requirements.
        """
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

    def clean_profile_picture(self):
        """
        Validates that the profile picture is not larger than 5MB.
        """
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture and profile_picture.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Profile picture size should not exceed 5 MB.")
        return profile_picture
