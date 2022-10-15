from datetime import datetime
from django.shortcuts import render

# from .forms import GeeksForm
from .models import GeeksModel

# importing formset_factory
# from django.forms import formset_factory
# from django.forms import modelformset_factory
# Create your views here.

from django.http import HttpResponse

#class based view - 300275126
from django.views.generic.list import ListView

class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel

    def get(self, request):
        context ={}

        # add the dictionary during initialization
        context["object_list"] = GeeksModel.objects.all()
        
        return render(request, "geeksmodel_list.html", context)

# creating form view
# def home_view(request):
#     context={}
#     context['form'] = InputForm()  # creating instance of InputForm and storing in context form property
#     return render(request, "home.html", context) # defined a templates folder in app level for keeping all templates at one place for specific app

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
    
    return render(request, "list_view.html", context)

# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

# def modelformset_view(request):
#     context ={}

#     GeeksFormSet = modelformset_factory(GeeksModel, fields=['title', 'description'], extra = 3)
#     formset = GeeksFormSet(request.POST)
#     if formset.is_valid():
#         for form in formset:
#             form.save()
#             print(form.cleaned_data)
#     # Add the formset to context dictionary
#     else: 
#         print("Not Valid")
#     context['formset']= formset
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "home.html", context)

# # creating view of form using modelsform
# def home_view(request):
#     context ={}
#     # create object of form
#     form = GeeksForm(request.POST or None, request.FILES or None)
    
#     # check if form data is valid
#     print(form.errors)
#     if form.is_valid():
#         # save the form data to model
#         form.save()
#         print(request.POST)
#     else:
#         print("Not Valid")
#     context['form']= form
    
#     return render(request, "home.html", context)
# # assignment 2 - Jai_300275126 - formsets
# def formset_view(request):
#     context ={}

#     # creating a formset
#     GeeksFormSet = formset_factory(GeeksForm, extra = 3) 
#     formset = GeeksFormSet(request.POST or None)
    
#     if formset.is_valid():
#         for form in formset:
#             form.save()
#             print(form.cleaned_data)
#     # Add the formset to context dictionary
#     else: 
#         print("Not Valid")
#     context['formset']= formset
    
#     return render(request, "home.html", context)