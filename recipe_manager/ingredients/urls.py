from django.urls import path

from . import views

app_name = 'ingredients'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('create', views.create, name='create'),
    # path('<int:pk>/edit', views.edit, name='edit'),
]
