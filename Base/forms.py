from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'age', 'gender', 'education', 'income', 'fees']
