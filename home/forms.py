from django import forms
from .models import Produit, Classe, Professeur, Matiere, Cours, Quiz, Question, Archives,Eleve

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

class Mat_eleve_form(forms.ModelForm):
    class Meta:
        model = Eleve
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
        
        
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'option1', 'option2', 'option3', 'option4', 'correct_option']
        

class archive_form(forms.ModelForm):
    class Meta:
        model = Archives
        fields = '__all__'