from django import forms

from .models import Thing #Import our model

class ThingForm(forms.ModelForm): #Create our form model based on our Thing

    class Meta:
        model = Thing
        fields = ('title', 'quit_date', 'cost_per_day', 'notes',) #User not included because that will be automatically populated