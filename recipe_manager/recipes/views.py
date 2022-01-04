from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views import generic
from ingredients.models import Ingredient, MeasurementUnits

from recipes.models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'newest_recipes'

    def get_queryset(self):
        """Return all recipes, optionally filtered by name"""
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(name__icontains=query).order_by('name')
        else:
            return Recipe.objects.all().order_by('name')


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


@login_required
def edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    all_ingredients = Ingredient.objects.all().order_by('name')
    all_measurement_units = MeasurementUnits.choices

    if request.method == 'POST':
        try:
            name = request.POST['name']

            recipe.name = name
            recipe.save()

            return render(request, 'recipes/edit_form.html', {
                'recipe': recipe,
                'all_ingredients': all_ingredients,
                'all_measurement_units': all_measurement_units,
                'success': 'The recipe was saved successfuly',
            })

        except Exception as e:
            return render(request, 'recipes/edit_form.html', {'recipe': recipe, 'error': str(e)})
    else:
        return render(request, 'recipes/edit_form.html', {
            'recipe': recipe,
            'all_ingredients': all_ingredients,
            'all_measurement_units': all_measurement_units,
        })
