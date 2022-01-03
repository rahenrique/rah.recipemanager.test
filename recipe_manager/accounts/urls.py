from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'login/', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
]
