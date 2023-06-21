from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('cards/', views.CardsList.as_view(), name="cards_list"),
    path('about/', views.About.as_view(), name="about"),
]