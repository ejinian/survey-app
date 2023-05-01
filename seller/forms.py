from django import forms
from .models import SellerSurveyResponse

class SellerSurveyForm(forms.ModelForm):
    class Meta:
        model = SellerSurveyResponse
        fields = ['store_name', 'balance', 'price', 'network', 'address', 'email']