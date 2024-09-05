from django.urls import path
#from .views import Display_Produit, accueil, cours
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
###################tests###########################

    path('display/',views.Display_Produit, name="display"),
    path('create/', views.product_create_view),
    path('update/<int:id>/',views.produit_update_view, name="update"),
    path('delete/<int:id>/',views.produit_delete_view, name="delete"),
    path('login',views.register_view,name="register_view"),
    path('login/',views.login_view, name="login_view"),
    
################### fin tests ###########################

################ Admin ##############

    path('indexadmin', views.indexadmin, name="indexadmin"),
    path('creer_matprof/',views.creer_matprof, name = "creer_matprof"),
    path('creer_mateleve/',views.creer_mateleve, name = "creer_mateleve"),
    path('creerclasse', views.creerClasse, name="creerclasse"),
    path('creer_matiere/',views.creer_matiere, name="creer_matiere"),
    
    

################# Proresseur #################
    path('index_prof', views.index_prof,name="index_prof" ),    
    path('creer_cours/',views.creer_cours, name="creer_cours"),
    
    
    
################# élève #################
    
    path('', views.index,name="index"),
    path('display_matiere/', views.display_matiere, name="display_matiere"),
    path('display_cours/', views.display_cours,name="display_cours"),
    path('details_cours/<str:slug>/', views.details_cours,name="details_cours"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    