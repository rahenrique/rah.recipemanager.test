from django.views import generic

from recipes.models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'newest_recipes'

    def get_queryset(self):
        """Return the newest recipes."""
        return Recipe.objects.order_by('-id')[:25]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
