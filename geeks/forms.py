from django import forms

#improting geeks/model from models.py
from .models import GeeksModel

# creating django form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")

    password = forms.CharField(widget=forms.PasswordInput())

# creating a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"
