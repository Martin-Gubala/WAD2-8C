from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('business', 'Business'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def save(self, comit=True):
        user = super().save(commit=False)
        if comit:
            user.save()
            UserProfile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
            return user
