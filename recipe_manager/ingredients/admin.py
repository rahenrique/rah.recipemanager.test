from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_measurement_unit', 'formatted_cost')


admin.site.register(Ingredient, IngredientAdmin)
