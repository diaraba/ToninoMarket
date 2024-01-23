from . import views
from django.contrib import admin
from django.urls import path, re_path
from .autocomplete import CategorieAutocomplete, ProduitAutocomplete, ClientAutocomplete,FournisseurAutocomplete
urlpatterns = [
    
    re_path(
        r'^categorie-autocomplete/$',
        CategorieAutocomplete.as_view(),
        name='categorie-autocomplete',
    ),
    
    re_path(
        r'^produit-autocomplete/$',
        ProduitAutocomplete.as_view(),
        name='produit-autocomplete',
    ),

    re_path(
        r'^client-autocomplete/$',
        ClientAutocomplete.as_view(),
        name='client-autocomplete',
    ),

    re_path(
        r'^fournisseur-autocomplete/$',
        FournisseurAutocomplete.as_view(),
        name='fournisseur-autocomplete',
    ),


    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
    path('accueil', views.accueil, name='accueil'),
    path('edit_client/<int:client_id>', views.edit_client, name='edit_client'), 
    path('liste_client', views.liste_client, name='liste_client'),
    path('detail_client/<int:id>', views.detail_client, name='detail_client'),
    path('delete_client/<int:id_client>', views.delete_client, name='delete_client'),
    path('achats_client/<int:id_client>', views.achats_client, name='achats_client'),
    path('ajouter_produit', views.ajouter_produit, name='ajouter_produit'),
    path('edit_produit/<int:id_produit>', views.edit_produit, name='edit_produit'),
    path('delete_produit/<int:id_produit>', views.delete_produit, name='delete_produit'),
    path('ajouter_categorie', views.ajouter_categorie, name='ajouter_categorie'),
    path('edit_categorie/<int:id_categorie>', views.edit_categorie, name='edit_categorie'), 
    path('categories', views.categories, name='categories'),
    path('categorie_detail/<int:id_categorie>', views.categorie_detail, name='categorie_detail'),
    path('delete_categorie/<int:id_categorie>', views.delete_categorie, name='delete_categorie'),
    path('categorie_produit/<int:id_categorie>', views.categorie_produit, name='categorie_produit'),
    path('ajouter_vente', views.ajouter_vente, name='ajouter_vente'),
    path('ventes', views.ventes, name='ventes'),
    path('vente_detail/<int:id_vente>', views.vente_detail, name='vente_detail'),
    path('delete_vente/<int:id_vente>', views.delete_vente,name='delete_vente'),
    path('edit_vente/<int:id_vente>', views.edit_vente,name='edit_vente'),
    path('ajouter_promotion', views.ajouter_promotion, name='ajouter_promotion'),
    path('promotions', views.promotions,name='promotions'),
    path('promotion_detail/<int:id_promotion>', views.promotion_detail, name='promotion_detail'),
    path('delete_promotion<int:id_promotion>', views.delete_promotion,  name='delete_promotion'),
    path('edit_promotion<int:id_promotion>', views.edit_promotion, name="edit_promotion"),
    path('ajouter_approvisionnement', views.ajouter_approvisionnement, name='ajouter_approvisionnement'),
    path('approvisionnements', views.approvisionnements, name='approvisionnements'),
    path('detail_approvisionnement/<int:id_approvisionnement>', views.detail_approvisionnement,name='detail_approvisionnement'),
    path('accuse_reception/<int:id_approvisionnement>', views.accuse_reception,name='accuse_reception'),
    path('alerte_ruptures', views.alerte_ruptures,name='alerte_ruptures'),
]
