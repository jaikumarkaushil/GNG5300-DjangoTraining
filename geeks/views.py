from datetime import datetime

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .forms import GeeksForm
from .models import GeeksModel

# importing formset_factory
# from django.forms import formset_factory
# from django.forms import modelformset_factory
# Create your views here.

from django.http import HttpResponse

#function based CRUD operations - 300275126
from django.views.generic.list import ListView

# function based create operation - 300275126
def create_view(request):
    context ={}
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    print(form.is_valid)
    if form.is_valid():
        form.save()
        print(form.instance.id)
    else:
        print("Not valid. Retry!")

    context['form']= form
    return render(request, "create_view.html", context)

class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel

    def get(self, request):
        context ={}

        # add the dictionary during initialization
        context["object_list"] = GeeksModel.objects.all()
        
        return render(request, "geeksmodel_list.html", context)

# CRUD - Retrieve using List
def list_view(request):
    context ={}
    context["dataset"] = GeeksModel.objects.all()
    
    return render(request, "list_view.html", context)

def detail_view(request, id):
    context ={}

    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
    print(context)
    return render(request, "detail_view.html", context)

# update view for details - 300275126
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)

    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("get/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)


    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)