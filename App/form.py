from django import forms
from .models import Portfolio

class MeuFormulario(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'

    python = forms.BooleanField(required=False, label='Python')
    java = forms.BooleanField(required=False, label='Java')
    css = forms.BooleanField(required=False, label='CSS')
    html = forms.BooleanField(required=False, label='HTML')
    javascript = forms.BooleanField(required=False, label='Java Script')
    c = forms.BooleanField(required=False, label='C')