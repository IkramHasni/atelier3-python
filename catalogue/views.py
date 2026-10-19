from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Category


def livre_list(request):
    livres = Book.objects.filter(price__lt=50).order_by("-publication_date")
    context = {
        "livres": livres,
        "titre_page": "Catalogue des livres",
    }
    return render(request, "catalogue/livre_list.html", context)


def livre_detail(request, pk):
    livre = get_object_or_404(Book, pk=pk)
    return render(request, "catalogue/livre_detail.html", {"livre": livre})


def auteur_list(request):
    auteurs = Author.objects.all().order_by("last_name", "first_name")
    return render(request, "catalogue/auteur_list.html", {"auteurs": auteurs})


def auteur_detail(request, pk):
    auteur = get_object_or_404(Author, pk=pk)
    livres = Book.objects.filter(author=auteur).order_by("title")
    context = {
        "auteur": auteur,
        "livres": livres,
        "nb_livres": livres.count(),
    }
    return render(request, "catalogue/auteur_detail.html", context)


def categorie_list(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "catalogue/categorie_list.html", {"categories": categories})