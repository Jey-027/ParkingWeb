from django import forms
from django.utils import timezone
from .models import InputRegister


class InputRegisterForm(forms.ModelForm):
    input = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), initial=timezone.now())

    class Meta:
        model = InputRegister
        fields = [
            "placa",
            "vehicle_type",
            "input"
        ]

        labels = {"vehicle_type_id": "Vehicle type",
                  "input": "Entry time"}
