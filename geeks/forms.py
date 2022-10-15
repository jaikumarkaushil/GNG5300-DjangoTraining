from django import forms

#improting geeks/model from models.py
from .models import GeeksModel

class GeeksForm(forms.Form):
    # model forms
    class Meta:
        model = GeeksModel
        fields = "__all__"

    # title = forms.CharField()
    # description = forms.CharField()
