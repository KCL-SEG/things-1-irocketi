from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'quantity', 'description']
        widgets = {'description': forms.Textarea()}
        
    # name, description, and quantity
    #name = forms.CharField(label='name', max_length=50)
    #decription = forms.Textarea()
    #quantity = forms.NumberInput()
    #description = forms.Textarea(widget=forms.Textarea)