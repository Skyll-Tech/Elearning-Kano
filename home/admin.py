from django.contrib import admin
from .models import Produit, Classe, Profil, Matiere, Professeur, Cours, Quiz
# Register your models here.

admin.site.register(Produit)
admin.site.register(Profil)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Professeur)
admin.site.register(Cours)
admin.site.register(Quiz)