from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review, UserProfile, Cafe, Drink

# Custom user registration form extending Django's UserCreationForm
class UserRegistrationForm(UserCreationForm):
    # Define userr type choices for registration
    USER_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('business', 'Business'),
    )
    # Fields for selecting user type during registration
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="Account Type")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def save(self, commit=True):
        # Save the form instance, create and link a UserProfile instance automatically
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        return user
    

# Form for updating existing user details
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Change Email")
    username = forms.CharField(required=True, label="Change Username")

    class Meta:
        model = User
        fields = ['username', 'email']

# Custom login form, inheriting  from Django's AuthenticationForm
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)

# Form for creating or updating a Cafe instance 
class CafeSetupForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'location', 'photo']  # Include photo field

# Form for creating or updating a Review instance
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        
# Form for editing an existing Cafe instance, used in the cafe detail page
class EditCafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'location']

# Form for creating or updating a Review instance
class DrinkReviewForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['rating']