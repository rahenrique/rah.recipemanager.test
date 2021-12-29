from django.contrib import admin

from .models import Recipe, RecipeIngredient


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_total_cost')
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
