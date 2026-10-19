from django.contrib import admin
# Register your models here.
from .models import Author, Book, Category

# Personnalisation de l'affichage pour les livres
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','price','publication_date')
    search_fields = ('title', 'summary')
    list_filter = ('publication_date','author','category')

# Enregistrement simple pour les auteurs
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'joined_date')
    search_fields = ('last_name', 'email')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')