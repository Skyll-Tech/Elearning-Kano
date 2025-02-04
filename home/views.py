from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produit, Classe, Professeur,Eleve, Prof_auth,Eleve,Eleve_auth, Matiere, Cours, Quiz, Question, Archives
from .forms import Produit_form, Classe_form, Mat_prof_form,Mat_eleve_form,  Matiere_form, Creer_Cours, archive_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

        user = User.objects.create_user(username=username, password=password, email=email)
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

######### Auth ###########


def register_admin(request):
    return render(request, "home/admin/auth/register.html")

def login_admin(request):
    return render(request,"home/admin/auth/login.html")



def admin_register(request):
    if request.method == "POST":
        admin_name = request.POST["admin_name"]
        admin_email = request.POST["admin_email"]
        admin_psw = request.POST["admin_psw"]
        confirm_psw = request.POST["confirm_psw"]
        
        if admin_psw != confirm_psw:
            messages.error(request, "Vos mots de passe ne correspondent pas!")
            return render(request, "home/admin/auth/register.html")
        
        if User.objects.filter(email=admin_email).exists():
            messages.error(request, "Ce compte existe deja!")
            return render(request, "home/admin/auth/register.html")

        user = User.objects.create_user(username=admin_name, password=admin_psw, email=admin_email)
        user.save()
        messages.success(request, "Votre compte à été creer avec succes")
        return redirect("admin_login")
    return render(request, "home/admin/auth/register.html")


def admin_login(request):
    if request.method == "POST":
        admin_name = request.POST["admin_name"]
        admin_psw = request.POST["admin_psw"]

        user = authenticate(request, username=admin_name, password=admin_psw)
        if user is not None:
            login(request, user)
            return redirect("indexadmin")
        else:
            messages.error(request, "Identifiant incorrect")
            return render(request, "home/admin/auth/login.html")
    return render(request, "home/admin/auth/login.html")

                #######

def register_prof(request):
    return render(request,"home/professeur/auth/register")

def login_prof(request):
    return render(request,"home/professeur/auth/login")

def prof_register(request):
    if request.method == "POST":
        mat_prof = request.POST["mat_prof"]
        prof_name = request.POST["prof_name"]
        prof_email = request.POST["prof_email"]
        prof_psw = request.POST["prof_psw"]
        confirm_psw_prof = request.POST["confirm_psw_prof"]
        
        if prof_psw != confirm_psw_prof:
            messages.error(request, "Vos mots de passe ne correspondent pas!")
            return render(request, "home/professeur/auth/register.html")


        
        if not Professeur.objects.filter(mat_prof=mat_prof).exists():
            messages.error(request, "Ce matricule n'existe pas!")
            return render(request, "home/professeur/auth/register.html")

        if User.objects.filter(email=prof_email).exists():
            messages.error(request, "Ce compte existe déjà!")
            return render(request, "home/professeur/auth/register.html")
        
        # Vérification de l'association e-mail/matricule
        if Prof_auth.objects.filter(mat_prof=mat_prof, prof_user__email=prof_email).exists():
            messages.error(request, "Cette adresse e-mail est déjà associée à ce matricule!")
            return render(request, "home/professeur/auth/register.html")
        
        # Vérification de l'existence du nom d'utilisateur
        if User.objects.filter(username=prof_name).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà!")
            return render(request, "home/professeur/auth/register.html")
            
        user = User.objects.create_user(username=prof_name, password=prof_psw, email=prof_email)
        user.save()
        
        # Création de l'entrée Prof_auth
        Prof_auth.objects.create(prof_user=user, mat_prof=mat_prof)
        
        messages.success(request, "Votre compte a été créé avec succès")
        return redirect("prof_login")
    return render(request, "home/professeur/auth/register.html")

      
def prof_login(request):
    if request.method == "POST":
        prof_name = request.POST["prof_name"]
        prof_psw = request.POST["prof_psw"]

        user = authenticate(request, username=prof_name, password=prof_psw)
        if user is not None:
            login(request, user)
            return redirect("matiere_prof")
        else:
            messages.error(request, "Identifiant incorrect")
            return render(request, "home/professeur/auth/login.html")
    return render(request, "home/professeur/auth/login.html")    

def logout_prof(request):
    logout(request)
    return redirect('login_prof')    

###############################


def eleve_register(request):
    if request.method == "POST":
        mat_eleve = request.POST["mat_eleve"]
        eleve_name = request.POST["eleve_name"]
        eleve_email = request.POST["eleve_email"]
        eleve_psw = request.POST["eleve_psw"]
        confirm_psw_eleve = request.POST["confirm_psw_eleve"]
        
        
        if not mat_eleve or not eleve_name or not eleve_email or not eleve_psw or not confirm_psw_eleve:
            messages.error(request, "Tous les champs sont obligatoires!")
            return render(request, "home/eleve/auth/register.html")
        
        if eleve_psw != confirm_psw_eleve:
            messages.error(request, "Vos mots de passe ne correspondent pas!")
            return render(request, "home/eleve/auth/register.html")
        
        if not Eleve.objects.filter(mat_eleve=mat_eleve).exists():
            messages.error(request, "Ce matricule n'existe pas!")
            return render(request, "home/eleve/auth/register.html")

        if User.objects.filter(email=eleve_email).exists():
            messages.error(request, "Ce compte existe déjà!")
            return render(request, "home/eleve/auth/register.html")
        
        if Eleve_auth.objects.filter(mat_eleve=mat_eleve, eleve_user__email=eleve_email).exists():
            messages.error(request, "Cette adresse e-mail est déjà associée à ce matricule!")
            return render(request, "home/eleve/auth/register.html")
        
        if User.objects.filter(username=eleve_name).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà!")
            return render(request, "home/eleve/auth/register.html")
            
        user = User.objects.create_user(username=eleve_name, password=eleve_psw, email=eleve_email)
        user.save()
        
        Eleve_auth.objects.create(eleve_user=user, mat_eleve=mat_eleve)
        
        messages.success(request, "Votre compte a été créé avec succès")
        return redirect("login_eleve")
    return render(request, "home/eleve/auth/register.html")     



def login_eleve(request):
    if request.method == "POST":
        eleve_name = request.POST["eleve_name"]
        eleve_psw = request.POST["eleve_psw"]

        user = authenticate(request, username=eleve_name, password=eleve_psw)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Identifiant incorrect")
            return render(request, "home/eleve/auth/login.html")
    return render(request, "home/eleve/auth/login.html")  

def logout_eleve(request):
    logout(request)
    return redirect('login_eleve') 



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
                    
            if len(mat_prof) != 9:
                messages.error(request, "La longueur du matricule doit être de 9 caractères")
                return redirect("creer_matprof")

            
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
    if request.method == "POST":
        form = Mat_eleve_form(request.POST)
        if form.is_valid():
            mat_eleve = form.cleaned_data["mat_eleve"]
                    
            if len(mat_eleve) != 9:
                messages.error(request, "La longueur du matricule doit être de 9 caractères")
                return redirect("creer_mateleve")

            
            if Eleve.objects.filter(mat_eleve=mat_eleve).exists():
                messages.error(request, "Ce matricule existe déjà!")
            else:
                form.save()
                messages.success(request, "Matricule crée avec succes!")
        return redirect("creer_mateleve")

    else:
        form = Mat_eleve_form()
    return render(request, "home/admin/creer_mateleve.html")


def creer_matiere(request):
    if request.method == "POST":
        form = Matiere_form(request.POST)
        if form.is_valid():
            nom_matiere = form.cleaned_data["nom_matiere"]  # La fonction "cleaned_data" est utilisée dans les formulaires Django pour accéder aux données validées et nettoyées après que le formulaire a été soumis et validé.
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
            nom_matiere = form.cleaned_data["nom_matiere"]
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

@login_required(login_url='/index_prof/')
def index_prof(request):
    cours = Cours.objects.all()
    context = {"cour": cours}
    return render(request, "home/professeur/index.html", context)

@login_required(login_url='/index_prof/')
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
                messages.success(request, "Cours créé avec succès!")
            return redirect("creer_cours")

    return render(request, "home/professeur/creer_cours.html", context)

@login_required(login_url='/index_prof/')
def matiere_prof(request):
    matiere = Matiere.objects.all()
    context = {"matieres": matiere}
    return render(request, "home/professeur/matiere_prof.html", context)

@login_required(login_url='/index_prof/')
def cours_prof(request, id_matiere_prof):
    matiere = get_object_or_404(Matiere, id=id_matiere_prof)
    cours = Cours.objects.filter(choix_matiere=matiere) # Permet d'indiqueer que nous voulons  filtrer les cours dont la matière correspond à l’objet matiere spécifié
    context = {"cours": cours, "matieres": matiere}  # Contexte pour le template
    return render(request, "home/professeur/cours_prof.html", context)  # Rendre le template avec le contexte

@login_required(login_url='/index_prof/')
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
            return redirect("matiere_prof")
    else:
        form = Creer_Cours(instance=cours)
    context = {"classe": classes, "matiere": matiere, "cours": cours, "form": form}
    return render(request, "home/professeur/modifier_cours.html", context)

@login_required(login_url='/index_prof/')
def delete_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    if request.method == "POST":
        cours.delete()
        return redirect("matiere_prof")

    return render(request, "home/professeur/delete_cours.html", {"cours": cours})


# Quizz

@login_required(login_url='/index_prof/')
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
    
@login_required(login_url='/index_prof/')
#voir les quizz
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'home/professeur/quizz/quiz_list.html', {'quizzes': quizzes})
# fin Quizz


# Archives
@login_required(login_url='/index_prof/')
def voir_archive(request):
    archive = Archives.objects.all()
    context = {"archive":archive}
    return render(request,'home/professeur/archives/archive.html',context)

def creer_archive(request):
    if request.method == "POST":
        form = archive_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Archive créée avec succès!")
            return redirect("archive")
        else:
            messages.error(request, "Erreur lors de la création de l'archive. Veuillez vérifier les informations fournies.")
    else:
        form = archive_form()
    return render(request, 'home/professeur/archives/creer_archive.html', {"form": form})


##################### élève #####################


def index(request):
    return render(request, "home/eleve/index.html")

@login_required(login_url='/login_eleve/')
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

