from django.db import models
# Create your models here.
from django.db import models

class Author(models.Model):
  first_name = models.CharField(max_length=100,verbose_name="Prénom")
  last_name = models.CharField(max_length=100,verbose_name="Nom")
  email = models.EmailField(unique=True, verbose_name="Adresse Email")
  joined_date = models.DateField(auto_now_add=True, verbose_name="Date d'inscription")
  def __str__(self):
      return f"{self.first_name} {self.last_name}"
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nom de la catégorie"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du livre")
    summary = models.TextField(blank=True, verbose_name="Résumé")
    publication_date = models.DateField(verbose_name="Date de publication")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix (TND)")
    # Relation Many-to-One : Un auteur peut écrire plusieurs livres
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books",verbose_name="Auteur",)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="books",verbose_name="Catégorie",null=True,blank=True)
    def __str__(self):
        return self.title