from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review, UserProfile, Cafe

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('business', 'Business'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        return user
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Change Email")
    username = forms.CharField(required=True, label="Change Username")

    class Meta:
        model = User
        fields = ['username', 'email']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)

class CafeSetupForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'location']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

class EditCafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'location']