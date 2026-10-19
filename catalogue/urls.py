from django.urls import path
from . import views
app_name = "catalogue"
urlpatterns = [
path("livres/", views.livre_list, name="livre_list"),
path("livres/<int:pk>/", views.livre_detail, name="livre_detail"),
path("auteurs/", views.auteur_list, name="auteur_list"),
path("auteurs/<int:pk>/", views.auteur_detail, name="auteur_detail"),
path("categories/", views.categorie_list, name="categorie_list"),
]