from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produit, Classe, Professeur, Matiere, Cours
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
    return render(request, "home/admin/index.html")


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
    return render(request, "home/admin/creer_matiere.html")


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
        form = Creer_Cours(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            if Cours.objects.filter(titre=titre).exists():
                messages.error(request, "Ce cours existe déjà!")
            else:
                form.save()
                messages.success(request, "Cours crée avec succes!")
            return redirect("creer_cours")

    return render(request, "home/professeur/creer_cours.html", context)



##################### élève #####################

def index(request):
    return render(request, "home/eleve/index.html")



def display_matiere(request):
    matiere = Matiere.objects.all()
    context = {"matieres":matiere}
    return render(request, "home/eleve/display_matiere.html", context)


def display_cours(request):
    cours = Cours.objects.all()
    context = {"cours":cours}
    return render(request, "home/eleve/display_cours.html", context)


def details_cours(request, slug):
    cours=get_object_or_404(Cours, slug=slug)
    context = {"cours": cours}
    return render(request, "home/eleve/details_cours.html", context)