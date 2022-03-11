from django import forms
from .models import Search

class Joinclass(forms.ModelForm):
    class Meta:
        model = Search
        fields = "__all__"
