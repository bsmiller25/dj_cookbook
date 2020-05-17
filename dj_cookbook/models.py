from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100,
                            choices=(('ct', 'Count'),
                                     ('cup', '1 Cup'),
                                     ('tbsp', 'TBSP'),
                                     ('tsp', 'TSP')),
                            default='cup')
    type = models.CharField(max_length=25,
                            choices=(('poultry', 'Poultry'),
                                     ('fish', 'Fish'),
                                     ('meat', 'Meat'),
                                     ('fruit', 'Fruit'),
                                     ('vegetable', 'Vegetable'),
                                     ('starch', 'Starch'),
                                     ('other', 'Other'))
                            )
    calories = models.FloatField()
    fat = models.FloatField()
    satfat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    
    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return(self.name)

class Meal(models.Model):
    name = models.CharField(max_length=100)
    winter = models.BooleanField(default=True)
    spring = models.BooleanField(default=True)
    summer = models.BooleanField(default=True)
    fall = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('meal-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return(self.name)
    
class Recipe(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    amount = models.FloatField(default=1)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    
    def __str__(self):
        return('{} - {} - {}'.format(self.meal, self.ingredient, self.amount))
    
