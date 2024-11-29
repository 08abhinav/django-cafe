from django import forms
from .models import Cafe

class UserInput(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ["name", "location", "open", "close", "coffee", "wifi", "powersockets"]

