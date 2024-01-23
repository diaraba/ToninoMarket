from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import ApprovisionnementForm, CategorieForm, ClientForm, ProduitForm, PromotionForm, VenteForm
from .models import AlerteRupture, Approvisionnement, Categorie, Client, Produit, Promotion, Vente
from django.contrib import messages


#verifier si l'utilisateur connecter est un gerant
def is_gerant(user):
    if user.groups.filter(name='Gerant').exists():
        return True
    
#verifier si l'utilisateur connecter est un caissier
def is_caissier(user):
    return user.groups.filter(name='Caissier ').exists()


def accueil(request):
    return render(request, 'market/accueil.html')

#nous avons ici les traitements lié aux informations du client
def ajouter_client(request):
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=Client()
        client=ClientForm(request.POST, instance=obj)  
        if client.is_valid():   
            client.save() 
            return redirect('liste_client')
        else:
            params = {
                'form': client,
                'gerant': gerant,
                'caissier': caissier
            }
            return render(request, 'market/client/ajouter_client.html', params)
    else:
        params = {
            'form': ClientForm(),
            'gerant': gerant,
            'caissier': caissier
        }
        return render(request, 'market/client/ajouter_client.html', params)

def edit_client(request, id_client):
    client = Client.objects.get(id=id_client)
    if (request.method == 'POST'):
        obj=client
        client_form=ClientForm(request.POST, instance=obj)  
        if client_form.is_valid():
            client_form.save()
            return redirect('accueil')  # 1
    else:
       params = {
            'client': client,
            'form': ClientForm(instance=client),
        }
       return render(request, 'market/client/edit_client.html', params)


def liste_client(request):
    clients = Client.objects.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'clients': clients,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/client/liste_client.html', params)

def detail_client(request, id):
    client = Client.objects.get(id=id)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)   

    params = {
        'client': client,
        'gerant': gerant,
        'caissier': caissier,
    }
    return render(request, 'market/client/detail_client.html', params)

def delete_client(request, id_client):

    client=Client.objects.get(id=id_client)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
            client.delete() 
            return redirect('liste_client')

    else:
        params = {
            'client': client,
            'gerant':gerant,
            'caissier':caissier,
        }
        return render(request, 'market/client/delete_client.html', params)

def achats_client(request, id_client):
    client = Client.objects.get(id=id_client)
    achats=client.achats.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'client': client,
        'achats':achats,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/client/achats_client.html', params)

#nous avons ici les traitements lié aux informations du model produit

def ajouter_produit(request):

    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=Produit()
        produit=ProduitForm(request.POST, instance=obj)  
        if produit.is_valid():   
            produit.save() 
            return redirect('accueil')
        else: 
            params = {
                'form': produit,
                'gerant': gerant,
                'caissier': caissier
            }
            return render(request, 'market/produit/ajouter_produit.html', params)            
    else:
        params = {
            'form': ProduitForm(),
            'gerant': gerant,
            'caissier': caissier
        }
        return render(request, 'market/produit/ajouter_produit.html', params)

def edit_produit(request, id_produit):

    produit=Produit.objects.get(id=id_produit)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=produit
        produit=ProduitForm(request.POST, instance=obj)  
        if produit.is_valid():   
            produit.save() 
            return redirect('accueil')
    else:
        params = {
            'form': ProduitForm(instance=produit),
            'gerant': gerant,
            'caissier': caissier,
            'produit': produit
        }
        return render(request, 'market/produit/edit_produit.html', params)

def delete_produit(request, id_produit):

    produit=Produit.objects.get(id=id_produit)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
            produit.delete() 
            return redirect('accueil')

    else:
        params = {
            'produit': produit
        }
        return render(request, 'market/produit/delete_produit.html', params)
        
def ajouter_categorie(request):

    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=Categorie()
        categorie=CategorieForm(request.POST, instance=obj)  
        if categorie.is_valid():   
            categorie.save() 
            return redirect('accueil')
        else:
            params = {
                'form': categorie,
                'gerant': gerant,
                'caissier': caissier
            }
            return render(request, 'market/produit/ajouter_categorie.html', params)
    else:
        params = {
            'form': CategorieForm(),
            'gerant': gerant,
            'caissier': caissier
        }
        return render(request, 'market/produit/ajouter_categorie.html', params)

def edit_categorie(request, id_categorie):

    categorie=Categorie.objects.get(id=id_categorie)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=categorie
        categorie_form=CategorieForm(request.POST, instance=obj)  
        if categorie_form.is_valid():   
            categorie_form.save() 
            return redirect('categories')
        else: 
            params = {
                'form': categorie_form,
                'gerant': gerant,
                'caissier': caissier,
                'categorie':categorie,
            }
            return render(request, 'market/produit/edit_categorie.html', params)           
    else:
        params = {
            'form': CategorieForm(instance=categorie),
            'gerant': gerant,
            'caissier': caissier,
            'categorie':categorie,
        }
        return render(request, 'market/produit/edit_categorie.html', params)

def delete_categorie(request, id_categorie):

    categorie=Categorie.objects.get(id=id_categorie)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
            categorie.delete() 
            return redirect('accueil')
    else:
        params = {
            'categorie': categorie
        }
        return render(request, 'market/produit/delete_categorie.html', params)

def categories(request):
    categories = Categorie.objects.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'categories': categories,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/produit/categories.html', params)

def categorie_detail(request, id_categorie):
    categorie = Categorie.objects.get(id=id_categorie)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'categorie': categorie,
        'gerant': gerant,
        'caissier': caissier,
    }
    return render(request, 'market/produit/categorie_detail.html', params)

def categorie_produit(request, id_categorie):
    categorie = Categorie.objects.get(id=id_categorie)
    produits=categorie.produits.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'produits': produits,
        'gerant': gerant,
        'caissier': caissier,
        'categorie': categorie,
    }

    return render(request, 'market/produit/categorie_produit.html', params)
#cette section cregroupe tout ce qui concerne la vente

def ajouter_vente(request):

    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    alerte_rupture=AlerteRupture()
    if (request.method == 'POST'):
        obj=Vente()
        form=VenteForm(request.POST, instance=obj)  
        if form.is_valid(): 
            vente = form.save(commit=False)
            if vente.quantite > vente.produit.quantite:
                params = {
                    'form': form,
                    'gerant': gerant,
                    'caissier': caissier
                }
                messages.add_message(request, messages.ERROR, 'La quantité demandé n\'est pas disponible')
                return render(request, 'market/vente/ajouter_vente.html', params)
            else:    
                vente.montant=vente.quantite*vente.produit.prix
                vente.caissier = request.user.caissier
                vente.save() 
                vente.produit.quantite=vente.produit.quantite-vente.quantite

            if vente.produit.quantite<=2:
                contenu = f'Votre stock de {vente.produit.designation} est presque epuisée veuillez vous approvisionner au plus vite'
                alerte_rupture.contenu=contenu
                alerte_rupture.save()
            vente.produit.save() 
            messages.add_message(request, messages.SUCCESS, 'L\'achat a été effectuer avec succes')
            return redirect('vente_detail', vente.id )
        else:
            params = {
                'form': form,
                'gerant': gerant,
                'caissier': caissier
            }
            return render(request, 'market/vente/ajouter_vente.html', params)
    else:
        params = {
            'form': VenteForm(),
            'gerant': gerant,
            'caissier': caissier
        }
        return render(request, 'market/vente/ajouter_vente.html', params)

def ventes(request):
    ventes = Vente.objects.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'ventes': ventes,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/vente/ventes.html', params)

def vente_detail(request, id_vente):
    vente = Vente.objects.get(id=id_vente)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'vente': vente,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/vente/vente_detail.html', params)

def delete_vente(request, id_vente):
    vente=Vente.objects.get(id=id_vente)
    if (request.method == 'POST'):
            vente.delete() 
            return redirect('ventes')
    else:
        params = {
            'vente': vente
        }
        return render(request, 'market/vente/delete_vente.html', params)

def edit_vente(request, id_vente):

    vente=Vente.objects.get(id=id_vente)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        obj=vente
        vente_form=VenteForm(request.POST, instance=obj)  
        if vente_form.is_valid():   
            if vente_form.quantite!=vente.quantite:
                vente.produit.quantite=vente.produit.quantite-vente_form.quantite
                vente.produit.save() 
            vente_form.save() 

            return redirect('categories')
        else:
            params = {
                'form': vente_form,
                'gerant': gerant,
                'caissier': caissier,
                'vente':vente,
            }
        return render(request, 'market/vente/edit_vente.html', params)
    else:
        params = {
            'form': VenteForm(instance=vente),
            'gerant': gerant,
            'caissier': caissier,
            'vente':vente,
        }
        return render(request, 'market/vente/edit_vente.html', params)


def promotions(request):
    promotions = Promotion.objects.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'promotions': promotions,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/vente/promotions.html', params)

def ajouter_promotion(request):

    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion= form.save()
            produits_selectionner = request.POST.getlist('produits') 
            promotion.produits.set(produits_selectionner)
            return redirect('accueil')
        else:
            params = {
                        'form': form,
                        'gerant': gerant,
                        'caissier': caissier
                    }
            return render(request, 'market/vente/ajouter_promotion.html', params)
           
    else:
        params = {
            'form': PromotionForm(),
            'gerant': gerant,
            'caissier': caissier
        }
        return render(request, 'market/vente/ajouter_promotion.html', params)


def promotion_detail(request, id_promotion):
    promotion = Promotion.objects.get(id=id_promotion)
    produits=promotion.produits.all()
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'promotion': promotion,
        'produits':produits,
        'gerant': gerant,
        'caissier': caissier,
    }
    return render(request, 'market/vente/promotion_detail.html', params)

def delete_promotion(request, id_promotion):
    promotion=Promotion.objects.get(id=id_promotion)
    if (request.method == 'POST'):
            promotion.delete() 
            return redirect('promotions')
    else:
        params = {
            'promotion': promotion,
        }
        return render(request, 'market/vente/delete_promotion.html', params)


def edit_promotion(request, id_promotion):
    
    promotion=Promotion.objects.get(id=id_promotion)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    
    if (request.method == 'POST'):
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            promotion= form.save()
            produits_selectionner = request.POST.getlist('produits') 
            promotion.produits.set(produits_selectionner)
            return redirect('accueil')
        else:
            params = {
                        'form': form,
                        'gerant': gerant,
                        'caissier': caissier,
                        'promotion': promotion,
                    }
            return render(request, 'market/vente/edit_promotion.html', params)
           
    else:
        params = {
            'form': PromotionForm(instance=promotion),
            'gerant': gerant,
            'caissier': caissier,
            'promotion': promotion,
        }
        return render(request, 'market/vente/edit_promotion.html', params)


def ajouter_approvisionnement(request):
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user) 

    if(request.method=='POST'):
        form=ApprovisionnementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories') 
        else:
            params={
                'form': ApprovisionnementForm(),
                'gerant':gerant,
                'caissier':caissier,
            } 
            return render(request, 'market/fournisseur/ajouter_approvisionnement.html',params)
    else:
        params={
            'form': ApprovisionnementForm(),
            'gerant':gerant,
            'caissier':caissier,
        } 
        return render(request, 'market/fournisseur/ajouter_approvisionnement.html',params)


def approvisionnements(request):
    approvisionnements=[]
    global_approvisionnements = Approvisionnement.objects.all()
    for approvisionnement in global_approvisionnements:
        if not approvisionnement.etat:
            approvisionnements.append(approvisionnement)
        
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'approvisionnements': approvisionnements,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/fournisseur/approvisionnements.html', params)

def detail_approvisionnement(request, id_approvisionnement):
    approvisionnement = Approvisionnement.objects.get(id=id_approvisionnement)
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)    

    params = {
        'approvisionnement': approvisionnement,
        'gerant': gerant,
        'caissier': caissier,
    }

    return render(request, 'market/fournisseur/detail_approvisionnement.html', params)

def accuse_reception(request, id_approvisionnement):
    approvisionnement=Approvisionnement.objects.get(id=id_approvisionnement)
    approvisionnement.etat=True
    approvisionnement.date_confirmation=datetime.now()
    approvisionnement.produit.quantite=approvisionnement.produit.quantite + approvisionnement.quantite
    approvisionnement.produit.save()
    approvisionnement.save()
    message = f'Votre stock en {approvisionnement.produit.designation} vient d\'être approvisionnée de {approvisionnement.quantite}  avec succès.'
    messages.add_message(request, messages.SUCCESS, message)
    return redirect('approvisionnements')


def alerte_ruptures(request):
    gerant=is_gerant(request.user)
    caissier=is_caissier(request.user)     
    global_alerte_ruptures=AlerteRupture.objects.all()
    alerte_ruptures=[]
    for alerte_rupture in global_alerte_ruptures:
        if not alerte_rupture.etat:
            alerte_ruptures.append(alerte_rupture)
    params={
        'alerte_ruptures': alerte_ruptures,
        'gerant': gerant,
        'caissier': caissier,        
    }    
    return render(request,'market/produit/alerte_ruptures.html', params)