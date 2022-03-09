from django.shortcuts import render
from .models import Search,Join
#from .forms import Formclass


# Create your views here.
def index(request,*args,**kwargs):
    return render(request, 'index.html',{})

def search(request,*args,**kwargs):
    if request.GET:
        bloodgroup = request.GET['bloodgroup']
        print("Blood :: " + bloodgroup)
        dist = request.GET['district']
        print("District :: " + dist)
        searchobj = Search.objects.filter(blood=bloodgroup,district=dist)
        search_context ={
           "searchobj" : searchobj
        }
        return render(request, 'search.html',search_context)
    else:
        print("Get not found \n"*10)
        return render(request, 'search.html')






'''
def form_create_view(request, *args,**kwargs):
    form=Formclass(request.POST or None)
    if form.is_valid():
        form.save()
        form=Formclass()
    context={
        'form': form,
    }
    return render(request, 'index.html', context)
'''

