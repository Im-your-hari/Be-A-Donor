from django.shortcuts import render
#from .forms import Formclass

# Create your views here.
def index(request,*args,**kwargs):
    return render(request, 'index.html',{})
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