from dal import autocomplete
from market.models import Categorie, Fournisseur, Produit,Client
from django.db.models import Q
from django.utils.html import format_html


class CategorieAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Categorie.objects.none()

        qs = Categorie.objects.all()

        if self.q:
                qs = qs.filter(Q(libelle__istartswith=self.q) | Q(code__istartswith=self.q) )

        return qs

    def get_result_label(self, item):
        
        return format_html('{} -- {}', item.code, item.libelle)
    

class ProduitAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Produit.objects.none()

        qs = Produit.objects.all()

        if self.q:
                qs = qs.filter(Q(designation__istartswith=self.q) | Q(categorie__libelle__istartswith=self.q))
        return qs
    
    def get_result_label(self, item):
        return format_html('{} - {}', item.designation, item.categorie)
    
class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Client.objects.none()

        qs = Client.objects.all()

        if self.q:
                qs = qs.filter(Q(code__istartswith=self.q))
        return qs

class FournisseurAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Fournisseur.objects.none()

        qs = Fournisseur.objects.all()

        if self.q:
                qs = qs.filter(Q(nom__istartswith=self.q) | Q(prenom__istartswith=self.q))
        return qs
