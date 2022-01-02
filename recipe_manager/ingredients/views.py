# from django.shortcuts import get_object_or_404, render
from django.views import generic

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


# def edit(request, pk):
#     ingredient = get_object_or_404(Ingredient, pk=pk)
#     return render(
#         request,
#         'ingredients/edit_form.html',
#         {'ingredient': ingredient}
#     )
