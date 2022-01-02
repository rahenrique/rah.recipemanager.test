from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_number', 'base_measurement_unit', 'formatted_cost')


admin.site.register(Ingredient, IngredientAdmin)
