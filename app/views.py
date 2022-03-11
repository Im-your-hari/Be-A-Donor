from django.shortcuts import render,redirect
from .models import Search,Join
from .forms import Joinclass


# Create your views here.
def index(request,*args,**kwargs):
    form=Joinclass(request.POST or None)
    if form.is_valid():
        form.save()
        form=Joinclass()
        return redirect('/')
    context={
        'form': form,
    }
    return render(request, 'index.html',context)

def search(request,*args,**kwargs):
    if request.POST:
        bloodgroup = request.POST['bloodgroup']
        print("Blood :: " + bloodgroup)
        dist = request.POST['district']
        print("District :: " + dist)
        searchobj = Search.objects.filter(blood=bloodgroup,district=dist)
        search_context ={
           "searchobj" : searchobj
        }
        return render(request, 'search.html',search_context)
    else:
        print("No data \n"*10)
        return render(request, 'index.html')

def form_create_view(request, *args,**kwargs):
    form=Joinclass(request.POST or None)
    if form.is_valid():
        form.save()
        form=Joinclass()
        return redirect('/')
    context={
        'form': form,
    }
    return render(request, 'index.html', context)
