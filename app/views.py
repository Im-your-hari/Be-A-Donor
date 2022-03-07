from django.shortcuts import render
from .models import Search,Join
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

searchobj = Search.objects.all()
search_context = {
    "searchobj" = searchobj,
}