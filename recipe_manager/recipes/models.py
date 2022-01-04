from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from common.services import convert_unit, value_to_unit, symbol_to_unit

from ingredients.models import Ingredient, MeasurementUnits


class Recipe(models.Model):
    class Meta:
        ordering = ('name', )
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    name = models.CharField(verbose_name='Recipe name', max_length=256)
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='Recipe ingredients', through='RecipeIngredient')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Recipe author')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Recipe created at')
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Recipe last updated at')

    def __str__(self) -> str:
        return self.name

    def total_cost(self) -> float:
        """Returns the total recipe cost, based on amount and cost of all ingredients."""
        cost = 0
        ingredient: Ingredient
        for ingredient in self.ingredients.all():
            cost += ingredient.recipeingredient_set.get().cost()
        return cost

    @admin.display(description='Total cost')
    def formatted_total_cost(self) -> str:
        """Returns the formatted total recipe cost."""
        return "€ {:.2f}".format(self.total_cost())


class RecipeIngredient(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['recipe', 'ingredient'], name="recipe_ingredient")]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    measurement_unit = models.CharField(
        max_length=2, choices=MeasurementUnits.choices)

    def cost(self):
        """Returns the ingredient cost for this recipe, based on amount and cost of ingredient."""
        ingredient_unit = self.ingredient.base_measurement_unit
        ingredient_cost = self.ingredient.minimal_cost()

        recipe_unit = self.measurement_unit
        recipe_amount = self.amount
        recipe_measure = value_to_unit(symbol=recipe_unit, value=recipe_amount)

        converted_recipe_measure = convert_unit(
            recipe_measure, symbol_to_unit(symbol=ingredient_unit))
        converted_recipe_amount = converted_recipe_measure.value

        return converted_recipe_amount * ingredient_cost

    def formatted_cost(self) -> str:
        """Returns the formatted ingredient cost for this recipe."""
        return "€ {:.2f}".format(self.cost())
