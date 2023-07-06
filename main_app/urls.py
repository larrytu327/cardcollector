from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('players/', views.PlayersList.as_view(), name="players_list"),
    path('about/', views.About.as_view(), name="about"),
    path('players/new/', views.PlayerCreate.as_view(), name="player_create"),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name="player_detail"),
    path('players/<int:pk>/update', views.PlayerUpdate.as_view(), name="player_update"),
    path('players/<int:pk>/delete', views.PlayerDelete.as_view(), name="player_delete"),
    path('players/<int:pk>/season_stats/new', views.Season_StatCreate.as_view(), name="season_stat_create"),
    path('myteam/<int:pk>/players/<int:player_pk>/', views.MyTeamPlayersAssoc.as_view(), name="myteam_player_assoc"),
]