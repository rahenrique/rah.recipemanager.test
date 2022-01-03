from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required

from ingredients.models import Ingredient


class IndexView(generic.ListView):
    template_name = 'ingredients/index.html'
    context_object_name = 'all_ingredients'

    def get_queryset(self):
        """Return all ingredients."""
        return Ingredient.objects.order_by('name')[:25]


class DetailView(generic.DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'


@login_required
def create(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            article_number = request.POST['article_number']
            base_measurement_unit = request.POST['base_measurement_unit']
            base_amount = request.POST['base_amount']
            cost_per_base_amount = request.POST['cost_per_base_amount']

            ingredient = Ingredient()
            ingredient.name = name
            ingredient.article_number = article_number
            ingredient.base_measurement_unit = base_measurement_unit
            ingredient.base_amount = base_amount
            ingredient.cost_per_base_amount = cost_per_base_amount
            ingredient.save()

            return redirect('ingredients:detail', pk=ingredient.id)

        except Exception as e:
            return render(request, 'ingredients/create_form.html', {'error': str(e)})
    else:
        return render(request, 'ingredients/create_form.html')


# def edit(request, pk):
#     ingredient = get_object_or_404(Ingredient, pk=pk)
#     return render(
#         request,
#         'ingredients/edit_form.html',
#         {'ingredient': ingredient}
#     )
