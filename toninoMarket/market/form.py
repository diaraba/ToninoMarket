from typing import Any
from django import forms
from .models import Approvisionnement, Categorie, Client, Produit, Promotion, Vente
from dal import autocomplete

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude =['code']
        
        widgets = {
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        error_messages = {
            'nom': {
                'required': 'Le nom ne peut pas être vide',  
            },
            'prenom':{
                'required': 'Le prenom ne peut pas être vide',
            },
            'adresse':{
                'required': 'L\'adresse ne peut pas être vide',
            },
            'telephone':{
                'required':'Le numero de telephone est obligatoire',
            },
        }
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['prenom'].widget.attrs.update({'class': 'form-control'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control'})
        self.fields['adresse'].widget.attrs.update({'class': 'form-control'})


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

        widgets = {
            'categorie': autocomplete.ModelSelect2(url='categorie-autocomplete')
        }
    
    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['categorie'].widget.attrs.update({'class': 'form-control'})
        self.fields['designation'].widget.attrs.update({'class': 'form-control'})
        self.fields['prix'].widget.attrs.update({'class': 'form-control'})


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategorieForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        self.fields['libelle'].widget.attrs.update({'class': 'form-control'})


class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields =[ 'produit','quantite', 'client']
        exclude =['date']
        widgets = {
            'produit': autocomplete.ModelSelect2(url='produit-autocomplete'),
            'client': autocomplete.ModelSelect2(url='client-autocomplete')
        }
        error_messages = {
            'client': {
                'required': 'Le client ne peut pas être vide',  
            },
            'produit':{
                'required': 'Le produit ne peut pas être vide',
            },
            'quantite':{
                'required':'La quantité doit être superieur ou égale a 1',
            },
        }
    
      
      
    def __init__(self, *args, **kwargs):
        super(VenteForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['produit'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantite'].widget.attrs.update({'class': 'form-control'})
        self.fields['client'].widget.attrs.update({'class': 'form-control'})


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = '__all__'

        widgets = {
            'produits': autocomplete.ModelSelect2Multiple(url='produit-autocomplete'),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

        error_messages = {
            'produits':{
                'required': 'Choisisez au moins un produit ',
            },
            'date_fin':{
                'required': 'La date de fin est obligatoire',
            },
            'date_debut':{
                'required': 'La date de début est obligatoire',
            },
            'pourcentage':{
                'required':'Le pourcentage est obligatoire',
                'min_value':'Le pourcentage doit être supérieur a 0.00',
                'max_value':'Le pourcentage doit être inférieur a 100.01',
            }, 
            'description':{
                'required': 'La description est obligatoire',
            },                       
        }
    
    def __init__(self, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['produits'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['pourcentage'].widget.attrs.update({'class': 'form-control'})


class ApprovisionnementForm(forms.ModelForm):
    class Meta:
        model = Approvisionnement
        fields =[ 'produit','titre','quantite', 'fournisseur']
        exclude =['date_demande', 'date_confirmation']
        widgets = {
            'produit': autocomplete.ModelSelect2(url='produit-autocomplete'),
            'fournisseur': autocomplete.ModelSelect2(url='fournisseur-autocomplete')
        }
        error_messages = {
            'fournisseur': {
                'required': 'Le fournisseur ne peut pas être vide',  
            },
            'produit':{
                'required': 'Le produit ne peut pas être vide',
            },
            'quantite':{
                'required':'La quantité doit être superieur ou égale a 1',
            },
        }
    
      
      
    def __init__(self, *args, **kwargs):
        super(ApprovisionnementForm, self).__init__(*args, **kwargs)
        # Ajoutez des classes Bootstrap aux champs du formulaire
        self.fields['produit'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantite'].widget.attrs.update({'class': 'form-control'})
        self.fields['fournisseur'].widget.attrs.update({'class': 'form-control'})
        self.fields['titre'].widget.attrs.update({'class': 'form-control'})

