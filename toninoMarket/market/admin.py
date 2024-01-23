from django.contrib import admin
from .models import Client, Fournisseur, Gerant,Caissier,Agent,Produit, Vente

class GerantAdmin(admin.ModelAdmin):
    list_display=('nom','prenom')

class CaissierAdmin(admin.ModelAdmin):
    list_display=('nom','prenom')


class AgentAdmin(admin.ModelAdmin):
    list_display=('nom','prenom')

class ClientAdmin(admin.ModelAdmin):
    list_display=('code','nom','prenom','telephone','adresse')

class ProduitAdmin(admin.ModelAdmin):
     list_display=('designation','prix', 'quantite', 'categorie')

class VenteAdmin(admin.ModelAdmin):
     list_display=('client','produit', 'caissier', 'quantite', 'montant','date')

class FournisseurAdmin(admin.ModelAdmin):
    list_display=('nom','prenom')

admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Vente, VenteAdmin)
admin.site.register(Produit, ProduitAdmin)   
admin.site.register(Gerant, GerantAdmin)
admin.site.register(Caissier, CaissierAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Client, ClientAdmin)
