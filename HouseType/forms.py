from django import forms
from .models import houseType

class HouseTypeForm(forms.ModelForm):
    class Meta:
        model = houseType
        fields = '__all__'