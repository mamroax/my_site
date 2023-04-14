from django import forms
from .models import Food

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['image']