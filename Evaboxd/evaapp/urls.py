from django.urls import path

from . import views

app_name = 'evaapp'
urlpatterns = [
    path('', views.IndexViews.as_view(), name="index"),
    path('<int:pk>/', views.ShowDetailViews.as_view(), name="show_details"),
    # path('<int:pk>/<int:pk>/', views.EpisodeDetailViews.as_view(), name="show_details")
]
