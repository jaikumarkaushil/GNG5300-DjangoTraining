from django import forms

#improting geeks/model from models.py
from .models import GeeksModel

# # creating django form
# class InputForm(forms.Form):
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")

#     password = forms.CharField(widget=forms.PasswordInput())

# # creating a ModelForm
# class GeeksForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = GeeksModel
#         fields = "__all__"

# creating a django form with widgets
class GeeksForm(forms.Form):
    # default widgets
    # title = forms.CharField()
    # description = forms.CharField()
    # views = forms.IntegerField()
    # available = forms.BooleanField()

    #custom widgets
    # title = forms.CharField(widget = forms.Textarea)
    # description = forms.CharField(widget = forms.CheckboxInput)
    # views = forms.IntegerField(widget = forms.TextInput)
    # available = forms.BooleanField(widget = forms.Textarea)

    # default widgets with custom datefield
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    date = forms.DateField(widget = forms.SelectDateWidget)
