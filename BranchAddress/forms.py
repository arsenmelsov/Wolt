from django import forms
from .models import BranchAddress

class BranchAddressForm(forms.ModelForm):
    class Meta:
        model = BranchAddress
        fields = '__all__'