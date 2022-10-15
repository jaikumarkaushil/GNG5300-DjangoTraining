from django.shortcuts import render
# from .forms import InputForm
from .forms import GeeksForm
# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Geeks")

# creating form view
# def home_view(request):
#     context={}
#     context['form'] = InputForm()  # creating instance of InputForm and storing in context form property
#     return render(request, "home.html", context) # defined a templates folder in app level for keeping all templates at one place for specific app


# creating view of form using modelsform
def home_view(request):
    context ={}
    # create object of form
    form = GeeksForm(request.POST or None, request.FILES or None)
    
    # check if form data is valid
    print(form.errors)
    if form.is_valid():
        # save the form data to model
        form.save()
        print(request.POST)
    else:
        print("Not Valid")
    context['form']= form
    
    return render(request, "home.html", context)