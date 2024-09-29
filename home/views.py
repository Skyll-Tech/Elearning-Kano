from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produit, Classe, Professeur, Matiere, Cours, Quiz, Question
from .forms import Produit_form, Classe_form, Mat_prof_form, Matiere_form, Creer_Cours
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def accueil(request):
    return HttpResponse("bonjour")


#  mes tests#

# def index (request):
#  return render(request, ("home/index.html"))


def Display_Produit(request):
    classes = Classe.objects.all()
    produits = Produit.objects.all()
    context = {"produit": produits, "classe": classes}
    return render(request, "home/display.html", context)


def product_create_view(request):
    if request.method == "POST":
        form = Produit_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("display")

    else:
        form = Produit_form()
    return render(request, "home/create.html", {"form": form})


def produit_update_view(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == "POST":
        form = Produit_form(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect("display")
    else:
        form = Produit_form(instance=produit)
    return render(request, "home/update.html", {"form": form, "produit": produit})


def produit_delete_view(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == "POST":
        produit.delete()
        return redirect("display")
    return render(request, "home/delete.html", {"produit": produit})


######### Auth ###########
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Vos mots de passe ne correspondent pas!")
            return render(request, "home/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce compte existe deja!")
            return render(request, "home/register.html")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Votre compte à été creer avec succes")
        return redirect("login_view")
    return render(request, "home/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("display")
        else:
            messages.error(request, "Identifiant incorrect")
            return render(request, "home/login.html")
    return render(request, "home/login.html")


# fin des tests


################# Admin #####################
def indexadmin(request):
    classe = Classe.objects.all()
    matiere = Matiere.objects.all()
    context = {"classe": classe, "matiere": matiere}
    return render(request, "home/admin/index_admin.html", context)


def creer_matprof(request):
    if request.method == "POST":
        form = Mat_prof_form(request.POST)
        if form.is_valid():
            mat_prof = form.cleaned_data["mat_prof"]
            if Professeur.objects.filter(mat_prof=mat_prof).exists():
                messages.error(request, "Ce matricule existe déjà!")
            else:
                form.save()
                messages.success(request, "Matricule crée avec succes!")
        return redirect("creer_matprof")

    else:
        form = Mat_prof_form()
    return render(request, "home/admin/creer_matprof.html")


def creer_mateleve(request):
    return render(request, "home/admin/creer_mateleve.html")


def creer_matiere(request):
    if request.method == "POST":
        form = Matiere_form(request.POST)
        if form.is_valid():
            nom_matiere = form.cleaned_data[
                "nom_matiere"
            ]  # La fonction "cleaned_data" est utilisée dans les formulaires Django pour accéder aux données validées et nettoyées après que le formulaire a été soumis et validé.
            if Matiere.objects.filter(nom_matiere=nom_matiere).exists():
                messages.error(request, "cette matière existe déjà!")
            else:
                form.save()
                messages.success(request, "Matière crée avec succes!")
            return redirect("creer_matiere")
    else:
        form = Matiere_form()
    return render(request, "home/admin/creer_matiere.html")


def update_matiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if request.method == "POST":
        form = Matiere_form(request.POST, instance=matiere)
        if form.is_valid():
            nom_matiere = form.cleaned_data[
                "nom_matiere"
            ]
            if Matiere.objects.filter(nom_matiere=nom_matiere).exists():
                messages.error(request, "cette matière existe déjà!")
            else:
                form.save()
                messages.success(request, "Matière modifiée avec succes!")
            return redirect("indexadmin")
    else:
        form = Matiere_form(instance=matiere)
    return render(request, "home/admin/update_matiere.html", {"form":form, "matiere": matiere})


def delete_matiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if request.method == "POST":
        matiere.delete()
        return redirect("indexadmin")
    return render(request, "home/admin/delete_matiere.html", {"matiere": matiere})


def creerClasse(request):
    if request.method == "POST":
        form = Classe_form(request.POST)
        if form.is_valid():
            nom_classe = form.cleaned_data["nom_Classe"]
            if Classe.objects.filter(nom_Classe=nom_classe).exists():
                messages.error(request, "cette classe existe déjà!")
            else:
                form.save()
                messages.success(request, "Classe crée avec succes!")
            return redirect("creerclasse")

    else:
        form = Classe_form()
    return render(request, "home/admin/creerclasse.html", {"form": form})


def update_classe(request, id):
    classe = get_object_or_404(Classe, id = id)
    if request.method == "POST":
        form = Classe_form(request.POST, instance = classe)
        if form.is_valid():
            nom_classe = form.cleaned_data["nom_Classe"]
            if Classe.objects.filter(nom_Classe=nom_classe).exists():
                messages.error(request, "cette classe existe déjà!")
            else:
                form.save()
                messages.success(request, "Classe crée avec succes!")
            return redirect("creerclasse")

    else:
        form = Classe_form(instance = classe)
    return render(request, "home/admin/update_classe.html", {"form": form, "classe":classe})


def delete_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        classe.delete()
        return redirect("indexadmin")
    return render(request, "home/admin/delete_classe.html", {"classe": classe})



##################### Professeur #####################


def index_prof(request):
    cours = Cours.objects.all()
    context = {"cour": cours}
    return render(request, "home/professeur/index.html", context)


def creer_cours(request):
    classes = Classe.objects.all()
    matiere = Matiere.objects.all()
    context = {"classe": classes, "matiere": matiere}

    if request.method == "POST":
        form = Creer_Cours(request.POST, request.FILES)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            if Cours.objects.filter(titre=titre).exists():
                messages.error(request, "Ce cours existe déjà!")
            else:
                form.save()
                messages.success(request, "Cours crée avec succes!")
            return redirect("creer_cours")

    return render(request, "home/professeur/creer_cours.html", context)



def matiere_prof(request):
    matiere = Matiere.objects.all()
    context = {"matieres": matiere}
    return render(request, "home/professeur/matiere_prof.html", context)


def cours_prof(request, id_matiere_prof):
    matiere = get_object_or_404(Matiere, id=id_matiere_prof)
    cours = Cours.objects.filter(choix_matiere=matiere) # Permet d'indiqueer que nous voulons  filtrer les cours dont la matière correspond à l’objet matiere spécifié
    context = {"cours": cours, "matieres": matiere}  # Contexte pour le template
    return render(request, "home/professeur/cours_prof.html", context)  # Rendre le template avec le contexte


def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    classes = Classe.objects.all()
    matiere = Matiere.objects.all()

    if request.method == "POST":
        form = Creer_Cours(request.POST, request.FILES, instance=cours)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            if Cours.objects.filter(titre=titre).exists():
                messages.error(request, "Ce cours existe déjà!")
            else:
                form.save()
                messages.success(request, "Cours modifier avec succes!")
            return redirect("cours_prof")
    else:
        form = Creer_Cours(instance=cours)
    context = {"classe": classes, "matiere": matiere, "cours": cours, "form": form}
    return render(request, "home/professeur/modifier_cours.html", context)


def delete_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    if request.method == "POST":
        cours.delete()
        return redirect("cours_prof")

    return render(request, "home/professeur/delete_cours.html", {"cours": cours})


# Quizz


def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Récupérer le titre du quiz
        num_questions = int(request.POST.get('num_questions'))  # Récupérer le nombre de questions
        quiz = Quiz.objects.create(title=title)  # Créer le quiz
        return redirect('add_questions', quiz_id=quiz.id, num_questions=num_questions)
    return render(request, 'home/professeur/quizz/create_quiz.html')  # Afficher le formulaire de création de quiz

# Vue pour ajouter des questions
def add_questions(request, quiz_id, num_questions):
    quiz = Quiz.objects.get(id=quiz_id)  # Récupérer le quiz
    question_numbers = range(num_questions)  # Générer une liste de nombres
    question_indices = [i + 1 for i in question_numbers]  # Ajuster les indices pour l'affichage

    # Combiner les listes en une seule liste de tuples
    combined_list = list(zip(question_numbers, question_indices))

    if request.method == 'POST':
        for i in question_numbers:
            text = request.POST.get(f'text_{i}')
            option1 = request.POST.get(f'option1_{i}')
            option2 = request.POST.get(f'option2_{i}')
            option3 = request.POST.get(f'option3_{i}')
            option4 = request.POST.get(f'option4_{i}')
            correct_option = request.POST.get(f'correct_option_{i}')
            Question.objects.create(
                quiz=quiz,
                text=text,
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                correct_option=correct_option
            )  # Créer chaque question
        return redirect('quiz_list')  # Rediriger vers la liste des quiz

    return render(request, 'home/professeur/quizz/add_questions.html', {
        'quiz': quiz,
        'combined_list': combined_list
    })  # Passer la liste combinée au template

#voir les quizz
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'home/professeur/quizz/quiz_list.html', {'quizzes': quizzes})



# fin Quizz


##################### élève #####################


def index(request):
    return render(request, "home/eleve/index.html")


def display_matiere(request):
    matiere = Matiere.objects.all()
    context = {"matieres": matiere}
    return render(request, "home/eleve/display_matiere.html", context)


def display_cours(request):
    cours = Cours.objects.all()
    context = {"cours": cours}
    return render(request, "home/eleve/display_cours.html", context)




def cours_par_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)  # Récupérer la matière ou renvoyer une erreur 404 si elle n'existe pas
    cours = Cours.objects.filter(choix_matiere=matiere)  # Filtrer les cours par la matière sélectionnée
    return render(request, 'home/eleve/cours_matiere.html', {'matiere': matiere, 'cours': cours})  # Rendre le template avec les cours filtrés





def details_cours(request, id_cours):
    cours = get_object_or_404(Cours, id=id_cours)
    context = {"cours": cours}
    return render(request, "home/eleve/details_cours.html", context)


#quizz

#repondre aux quizz
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option == question.correct_option:
                score += 1
        return redirect('quiz_result', quiz_id=quiz.id, score=score, total=total_questions)
    return render(request, 'home/eleve/quizz/take_quiz.html', {'quiz': quiz, 'questions': questions})

# affiche les resultats
def quiz_result(request, quiz_id, score, total):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'home/eleve/quizz/quiz_result.html', {'quiz': quiz, 'score': score, 'total': total})

#fin quizz
