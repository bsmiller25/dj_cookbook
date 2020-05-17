from django.urls import path

from dj_cookbook import views

app_name='cookbook'
urlpatterns = [
    path('', views.index, name='index'),
    #ingredients
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/all/', views.IngredientList.as_view(), name='ingredient-list'),
    path('ingredients/<pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients/<pk>/update', views.IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredients/<pk>/delete', views.IngredientDelete.as_view(), name='ingredient-delete'),
    #meals
    path('meals/create/', views.MealCreate.as_view(), name='meal-create'),
    path('meals/all/', views.MealList.as_view(), name='meal-list'),
    path('meals/add-recipe/', views.meal_add_recipe, name='meal-add-recipe'),
    path('meals/<pk>/', views.MealDetail.as_view(), name='meal-detail'),
    path('meals/<pk>/update', views.MealUpdate.as_view(), name='meal-update'),
    path('meals/<pk>/delete', views.MealDelete.as_view(), name='meal-delete'),
    #recipes
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/all/', views.RecipeList.as_view()),
    path('recipes/<pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/<pk>/update', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<pk>/delete', views.RecipeDelete.as_view(), name='recipe-delete'),
]

