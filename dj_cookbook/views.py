from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from dj_cookbook.models import *
import dj_cookbook.forms as forms
import pdb

def index(request):
    return render(request, 'dj_cookbook/index.html')

    
class IngredientCreate(CreateView):
    model = Ingredient
    fields = "__all__"

class IngredientDetail(DetailView):
    model = Ingredient

class IngredientList(ListView):
    model = Ingredient
    
class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = "__all__"

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url="/cookbook/"

class MealCreate(CreateView):
    model = Meal
    fields = "__all__"

class MealDetail(DetailView):
    model = Meal
    def get_context_data(self, **kwargs):
        context = super(MealDetail, self).get_context_data(**kwargs)
        context['mealRecipeForm'] = forms.MealRecipeForm()
        return context
    
@login_required    
def meal_add_recipe(request):
    meal = Meal.objects.get(pk=request.POST.get('meal'))
    ingredient = Ingredient.objects.get(pk=request.POST.get('ingredient'))
    amount = request.POST.get('amount')

    Recipe.objects.get_or_create(
        meal=meal,
        ingredient=ingredient,
        amount=amount)

    return(HttpResponse(True))
    
class MealList(ListView):
    model = Meal
    
class MealUpdate(UpdateView):
    model = Meal
    fields = "__all__"

class MealDelete(DeleteView):
    model = Meal
    success_url="/cookbook/"

class RecipeCreate(CreateView):
    model = Recipe
    fields = "__all__"

class RecipeDetail(DetailView):
    model = Recipe

class RecipeList(ListView):
    model = Recipe

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = "__all__"

class RecipeDelete(DeleteView):
    model = Recipe
    success_url="/cookbook/"

    
