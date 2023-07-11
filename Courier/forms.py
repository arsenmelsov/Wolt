from django import forms
from .models import Courier

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'