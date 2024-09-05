from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#######################################tests###############################

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)
    prix_actuel = models.DecimalField(max_digits=10, decimal_places=2)
    prix_promo = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.nom


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    email = models.EmailField()
    
    def __str__(self):
        return self.user.username
    
    
    
    
###########################################fin tests###############################""

##################### Model admin ############################

class Classe(models.Model):
    nom_Classe = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom_Classe
    

class Professeur(models.Model):
    mat_prof = models.CharField(max_length=15)
    
    def __str__(self):
        return self.mat_prof
    

class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nom_matiere
    
    

##################### Model Professeur ############################

class Cours(models.Model):
    
    titre = models.CharField(max_length=255)
    intoduction = models.TextField(null=True, blank=True)
    resume = models.TextField()
    choix_matiere = models.ForeignKey ('Matiere', on_delete=models.CASCADE)
    choix_classe = models.ForeignKey ('Classe', on_delete=models.CASCADE)
    #temps = models.TimeField()
    Date_creation = models.DateTimeField(auto_now_add=True)  # Date et heure de création
    Date_modif = models.DateTimeField(auto_now=True)  # Date et heure de mise à jour
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.titre