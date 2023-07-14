from django import forms
from .models import ReccomendedFood

class ReccomendedFoodForm(forms.ModelForm):
    class Meta:
        model = ReccomendedFood
        fields = '__all__'