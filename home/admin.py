from django.contrib import admin
from .models import Produit, Classe, Profil, Matiere, Professeur,Archives, Cours, Quiz, Admin_auth,Eleve_auth,Eleve
# Register your models here.

admin.site.register(Produit)
admin.site.register(Profil)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Professeur)
admin.site.register(Cours)
admin.site.register(Quiz)
admin.site.register(Archives)
admin.site.register(Admin_auth)
admin.site.register(Eleve_auth)
admin.site.register(Eleve)