from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # download data
    path('download/', views.download),
    path('cast/', views.cast),
    path('provider/', views.provider),
    path('providerlink/', views.providerlink),
    path('genre/', views.genre),

    #json
    path('movielist/', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail')
]