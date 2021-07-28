from django.urls import path
from . import views

# url configuration for view.index function
app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),  # represents a root of this app
    path('<int:movie_id>', views.detail, name='detail')
]
