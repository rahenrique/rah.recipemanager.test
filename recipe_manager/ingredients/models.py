from django.contrib import admin
from django.db import models

from common.models import Centiliter, Gram, Kilogram, Liter


class MeasurementUnits(models.TextChoices):
    GRAMS = Gram.symbol, 'grams'
    KILOGRAMS = Kilogram.symbol, 'kilograms'
    CENTILITER = Centiliter.symbol, 'centiliter'
    LITER = Liter.symbol, 'liter'


class Ingredient(models.Model):
    class Meta:
        ordering = ('name', 'article_number')
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    name = models.CharField(verbose_name='Ingredient name', max_length=256)
    article_number = models.CharField(
        verbose_name='Article number', max_length=24)
    base_measurement_unit = models.CharField(
        verbose_name='Measurement Unit', max_length=2, choices=MeasurementUnits.choices)
    base_amount = models.FloatField(verbose_name='Buying Amount', default=0)
    cost_per_base_amount = models.DecimalField(
        verbose_name='Cost per buying amount', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def minimal_cost(self) -> float:
        """
        Returns the ingredient cost for the minimum amount.
        Example:
        If the 'buying amount' is 2kg, and the 'cost per buying amount' is 1.00 EUR,
        the 'minimal cost' will return 0.50 EUR
        """
        return float(self.cost_per_base_amount) / self.base_amount

    @admin.display(description='Cost/amount')
    def formatted_cost(self) -> str:
        """Returns the formatted ingredient cost."""
        return f'{self.cost_per_base_amount} EUR / \
            {self.base_amount} {self.base_measurement_unit}'
