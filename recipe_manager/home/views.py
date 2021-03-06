from django.shortcuts import render

from recipes.models import Recipe
from ingredients.models import Ingredient


def index(request):
    return render(
        request,
        'home/index.html',
        {
            'newest_recipes': Recipe.objects.order_by('-created_at')[:3],
            'newest_ingredients': Ingredient.objects.order_by('-id')[:3],
        }
    )
