from django.shortcuts import render
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
        name = request.POST['name']
        article_number = request.POST['article_number']
        Ingredient.objects.create({'name': name, 'article_number': article_number})
        # return render(request, 'ingredients/create_form.html')
        return
    else:
        return render(request, 'ingredients/create_form.html')


# def edit(request, pk):
#     ingredient = get_object_or_404(Ingredient, pk=pk)
#     return render(
#         request,
#         'ingredients/edit_form.html',
#         {'ingredient': ingredient}
#     )
