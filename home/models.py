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
    profil_cours = models.ImageField(upload_to='image', null=True, blank=True)
    intoduction = models.TextField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    choix_matiere = models.ForeignKey ('Matiere', on_delete=models.CASCADE)
    choix_classe = models.ForeignKey ('Classe', on_delete=models.CASCADE)
    #temps = models.TimeField()
    Date_creation = models.DateTimeField(auto_now_add=True)  # Date et heure de création
    Date_modif = models.DateTimeField(auto_now=True)  # Date et heure de mise à jour
    temps_etudes = models.IntegerField()
    def __str__(self):
        return self.titre
    
    
    


# Modèle pour le quiz
class Quiz(models.Model):
    title = models.CharField(max_length=200)  # Titre du quiz

# Modèle pour les questions
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # Référence au quiz
    text = models.CharField(max_length=200)  # Texte de la question
    option1 = models.CharField(max_length=200)  # Option 1
    option2 = models.CharField(max_length=200)  # Option 2
    option3 = models.CharField(max_length=200)  # Option 3
    option4 = models.CharField(max_length=200)  # Option 4
    correct_option = models.CharField(max_length=200)  # Option correcte
