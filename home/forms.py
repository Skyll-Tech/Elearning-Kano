from django import forms
from .models import Produit, Classe, Professeur, Matiere, Cours

class Produit_form(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__' #['nom','quantite','image'] # si on a besoin de tout les champs on peut juste faire: fields = '__all__'
        
        
################ Admin ###########################
   
    
class Classe_form(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'


class Mat_prof_form(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = '__all__'
    

class Matiere_form(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = '__all__'
        
        
        
        
################ Professeur ###########################

class Creer_Cours(forms.ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'