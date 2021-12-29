from django.contrib import admin
from django.db import models


class Ingredient(models.Model):

    class MeasurementUnits(models.TextChoices):
        GRAMS = 'g', 'grams'
        KILOGRAMS = 'kg', 'kilograms'
        CENTILITER = 'cl', 'centiliter'
        LITER = 'l', 'liter'

    name = models.CharField(max_length=256)
    article_number = models.IntegerField()
    base_amount = models.FloatField(default=0)
    amount_unit = models.CharField(max_length=2, choices=MeasurementUnits.choices)
    cost_per_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @admin.display(
        # boolean=True,
        # ordering='pub_date',
        description='Cost/amount',
    )
    def formatted_cost(self):
        return f'€ {self.cost_per_amount} / {self.base_amount} {self.amount_unit}'


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()

# Example: The ingredient “carrot” has a cost of 1 EURO per 500 grams.
# You need to minimally support the following units: ‘grams’, ‘kilograms’, ‘centiliter’, ‘liter’.
