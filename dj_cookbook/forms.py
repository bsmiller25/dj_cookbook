from django import forms
from .models import *

   
class MealRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['ingredient', 'amount']

        
