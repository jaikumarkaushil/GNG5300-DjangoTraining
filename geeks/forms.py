from django import forms

#improting geeks/model from models.py
from .models import GeeksModel

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"
