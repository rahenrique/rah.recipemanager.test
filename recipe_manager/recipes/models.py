from django.contrib import admin
from django.db import models

from ingredients.models import Ingredient, MeasurementUnits


class Recipe(models.Model):
    class Meta:
        ordering = ('name', )
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    name = models.CharField(verbose_name='Recipe name', max_length=256)
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='Recipe ingredients', through='RecipeIngredient')

    def __str__(self) -> str:
        return self.name

    def total_cost(self) -> float:
        """Returns the total recipe cost, based on amount and cost of all ingredients."""
        cost = 0
        ingredient: Ingredient
        for ingredient in self.ingredients.all():
            ingredient_cost = ingredient.minimal_cost()
            recipe_amount = ingredient.recipeingredient_set.get().amount
            recipe_cost = ingredient_cost * recipe_amount
            cost += recipe_cost
        return cost

    @admin.display(description='Total cost')
    def formatted_total_cost(self) -> str:
        """Returns the formatted total recipe cost."""
        return f'€ {self.total_cost()}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    measurement_unit = models.CharField(
        max_length=2, choices=MeasurementUnits.choices)
