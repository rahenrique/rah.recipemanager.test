from django.contrib import admin
from django.db import models

from ingredients.models import Ingredient, MeasurementUnits


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredient')

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def total_cost(self) -> float:
        cost = 0
        ingredient: Ingredient
        for ingredient in self.ingredients.all():
            ingredient_cost = ingredient.minimal_cost()
            recipe_amount = ingredient.recipeingredient_set.get().amount
            recipe_cost = recipe_amount * ingredient_cost
            cost += recipe_cost
        return cost

    @admin.display(description='Total cost')
    def formatted_total_cost(self) -> str:
        return f'€ {self.total_cost()}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    measurement_unit = models.CharField(
        max_length=2, choices=MeasurementUnits.choices)
