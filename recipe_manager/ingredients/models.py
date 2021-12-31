from django.contrib import admin
from django.db import models


class MeasurementUnits(models.TextChoices):
    GRAMS = 'g', 'grams'
    KILOGRAMS = 'kg', 'kilograms'
    CENTILITER = 'cl', 'centiliter'
    LITER = 'l', 'liter'


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    base_measurement_unit = models.CharField(
        max_length=2, choices=MeasurementUnits.choices)
    base_amount = models.FloatField(default=0)
    cost_per_base_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def minimal_cost(self) -> float:
        return float(self.cost_per_base_amount) / self.base_amount

    @admin.display(description='Cost/amount')
    def formatted_cost(self) -> str:
        return f'{self.cost_per_base_amount} EUR / \
            {self.base_amount} {self.base_measurement_unit}'
