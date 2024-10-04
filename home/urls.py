from django.urls import path
#from .views import Display_Produit, accueil, cours
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
###################tests###########################

    path('display/',views.Display_Produit, name="display"),
    path('createproduit/', views.product_create_view),
    path('update/<int:id>/',views.produit_update_view, name="update"),
    path('delete/<int:id>/',views.produit_delete_view, name="delete"),
    path('login',views.register_view,name="register_view"),
    path('login/',views.login_view, name="login_view"),
    
################### fin tests ###########################

################ Admin ##############

    path('indexadmin/', views.indexadmin, name="indexadmin"),
    path('creer_matprof/',views.creer_matprof, name = "creer_matprof"),
    path('creer_mateleve/',views.creer_mateleve, name = "creer_mateleve"),
    
    path('creerclasse/', views.creerClasse, name="creerclasse"),
    path('update_classe/<int:id>/',views.update_classe, name="update_classe"),
    path('delete_classe/<int:id>/', views.delete_classe, name="delete_classe"),
    
    path('creer_matiere/',views.creer_matiere, name="creer_matiere"),
    path('update_matiere/<int:id>/',views.update_matiere, name="update_matiere"),
    path('delete_matiere/<int:id>/', views.delete_matiere, name="delete_matiere"),
    
    path('login_admin/', views.login_admin, name="login_admin"),
    path('register_admin/', views.register_admin, name="register_admin"),

    

################# Professeur #################
    path('index_prof/', views.index_prof,name="index_prof" ),    
    path('creer_cours/', views.creer_cours, name="creer_cours"),
    path('matiere_prof/', views.matiere_prof, name="matiere_prof"),
    path('cours_prof/', views.cours_prof, name="cours_prof"),
    path('modifier_cours/<int:id>/',views.modifier_cours, name="modifier_cours"),
    path('delete_cours/<int:id>/', views.delete_cours, name="delete_cours"),
    path('cours_matiere_prof/<int:id_matiere_prof>/', views.cours_prof, name='cours_matiere_prof'),
    path("creer_archive/", views.creer_archive, name="creer_archive"),
    path("archive/", views.voir_archive, name="archive"),
    #quizz
    path('create/', views.create_quiz, name='create_quiz'),
    path('add_questions/<int:quiz_id>/<int:num_questions>/', views.add_questions, name='add_questions'),
    path('quiz-list/', views.quiz_list, name='quiz_list'),
    path('take-quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('quiz-result/<int:quiz_id>/<int:score>/<int:total>/', views.quiz_result, name='quiz_result'),
    

      
    
################# élève #################
    
    path('', views.index,name="index"),
    path('display_matiere/', views.display_matiere, name="display_matiere"),
    path('display_cours/', views.display_cours,name="display_cours"),
    path('details_cours/<int:id_cours>/', views.details_cours, name="details_cours"),
    path('matiere/<int:matiere_id>/', views.cours_par_matiere, name='cours_par_matiere'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    