from django.views import generic

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
