from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_cost')


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
