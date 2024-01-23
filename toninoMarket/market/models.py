from datetime import date
import random
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError


class Client(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom")
    code=models.CharField(max_length=255, verbose_name="Code client", default=None , unique=True, editable=False, null=True, blank=True)
    prenom = models.CharField(max_length=255, verbose_name="Prénom")
    telephone=models.CharField(max_length=8, verbose_name="Telephone", unique=True)
    adresse=models.CharField(max_length=255, verbose_name="Adresse") 
    date_naissance=models.DateField(verbose_name="Date de naissance", default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.code+ " "+" "+self.nom+ " "+" "+self.prenom}'
    
    def code_unique(self):
        while True:
            # Generer un nombre aleatoire
            nbre_aleatoire = random.randint(1000, 9999)

            # Combine les initiales du nom et du prenom avec un nombre aleatoire
            code = f'{self.nom[:2]}{self.prenom[:2]}{nbre_aleatoire}'
            # Check if the generated code already exists in the database
            if not Client.objects.filter(code=code).exists():
                return code

    def save(self, *args, **kwargs):
        # Generate a unique code when saving the object
        if not self.code:
            self.code = self.code_unique()
        super().save(*args, **kwargs)



class Personnel(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom")
    prenom = models.CharField(max_length=255, verbose_name="Prénom")
    telephone=models.CharField(max_length=8, verbose_name="Telephone")
    adresse=models.CharField(max_length=255, verbose_name="Adresse") 
    age=models.PositiveIntegerField(verbose_name="age",default=0,blank=True)
    def __str__(self):
        return f'{self.nom+ " ", +""+self.prenom}'

class Gerant(Personnel):

    user = models.OneToOneField(User,related_name="gerant" ,on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Assigner l'utilisateur au groupe des médecins
        gerant_group, created = Group.objects.get_or_create(name='Gerant')

        # Vérifier si le groupe a été créé lors de cette opération
        if created:
            # Ajouter les autorisations nécessaires au groupe ici si besoin
            pass

        # Vérifier si l'utilisateur n'appartient pas déjà au groupe
        if not self.user.groups.filter(name='Gerant').exists():
            self.user.groups.add(gerant_group)
            
        self.user.is_staff = True
        self.user.save()
    def __str__(self):
        return f'{self.prenom+""+self.nom}'

class Caissier(Personnel):

    user = models.OneToOneField(User,related_name="caissier" ,on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Assigner l'utilisateur au groupe des médecins
        caissier_group, created = Group.objects.get_or_create(name='Caissier')

        # Vérifier si le groupe a été créé lors de cette opération
        if created:
            # Ajouter les autorisations nécessaires au groupe ici si besoin
            pass

        # Vérifier si l'utilisateur n'appartient pas déjà au groupe
        if not self.user.groups.filter(name='Caissier').exists():
            self.user.groups.add(caissier_group)
            
        self.user.is_staff = True
        self.user.save()
    def __str__(self):
        return f'{self.prenom+""+self.nom}'


class Agent(Personnel):

    user = models.OneToOneField(User,related_name="agent" ,on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Assigner l'utilisateur au groupe des médecins
        agent_group, created = Group.objects.get_or_create(name='Agent')

        # Vérifier si le groupe a été créé lors de cette opération
        if created:
            # Ajouter les autorisations nécessaires au groupe ici si besoin
            pass

        # Vérifier si l'utilisateur n'appartient pas déjà au groupe
        if not self.user.groups.filter(name='Agent').exists():
            self.user.groups.add(agent_group)
            
        self.user.is_staff = True
        self.user.save()
    def __str__(self):
        return f'{self.prenom+""+self.nom}'

class Categorie(models.Model):
    code = models.CharField(max_length=255, verbose_name="code")
    libelle = models.CharField(max_length=255, verbose_name="Libelle")
    def __str__(self):
        return f'{self.libelle}'

class Produit(models.Model):
    designation = models.CharField(max_length=255, verbose_name="designation")
    prix=models.fields.DecimalField(max_digits=10,decimal_places=2, verbose_name="Prix")
    quantite=models.PositiveIntegerField(verbose_name="quantite",default=0,blank=True)   
    categorie=models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True,blank=True,related_name='produits',verbose_name='Categorie')

    def __str__(self):
        return f'{self.designation}'

class Vente(models.Model):
    date = models.DateTimeField(verbose_name="Date de vente", auto_now_add=True)
    quantite=models.fields.DecimalField(max_digits=10,decimal_places=2, verbose_name="Quantite",validators=[MinValueValidator(1),])
    montant=models.fields.DecimalField(max_digits=10,decimal_places=2, verbose_name="Montant")
    caissier=models.ForeignKey(Caissier, on_delete=models.SET_NULL, null=True,blank=True,related_name='ventes',verbose_name='Caissier')
    produit=models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True,related_name='ventes',verbose_name='Produit')
    client=models.ForeignKey(Client, on_delete=models.SET_NULL, null=True,related_name='achats',verbose_name='Client')
    class Meta:
        ordering = ['-date']

    def montant_vente(self):
        if self.produit and self.produit.promotions.exists():
            pourcentages=0
            i=0
            for promotion in self.produit.promotions.all():
                i=i+1
                print("---------------------------------"+str(i))
                print(date.today())
                print("---------------------------------" + str(i))
                print(promotion.date_debut)
                if promotion.date_debut<=date.today() and promotion.date_fin>=date.today():
                    pourcentages= pourcentages + promotion.pourcentage
                    print("---------------------------------"+str(i))
                    print(date.today())
                    print("---------------------------------"+str(i))
                    print(promotion.date_debut)
                else:
                    pourcentages= pourcentages + 0
        
            if pourcentages>0:
                pourcentage=pourcentages/100
                montant_reduit = self.montant * (1 - pourcentage)
            else:
                montant_reduit = self.montant                 

            return round(montant_reduit, 2)
        else:
            # Sinon, utilisez le montant normal
            return round(self.montant, 2)

    def save(self, *args, **kwargs):
        self.montant = self.montant_vente()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.date} - {self.quantite} - {self.montant}'


class Fournisseur(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom")
    prenom = models.CharField(max_length=255, verbose_name="Prénom")
    telephone=models.CharField(max_length=8, verbose_name="Telephone")
    adresse=models.CharField(max_length=255, verbose_name="Adresse") 
    produits=models.ManyToManyField(Produit,related_name="fournisseurs",through="Approvisionnement")

    def __str__(self):
        return f'{self.nom+ "  " +self.prenom}'

class Approvisionnement(models.Model):
    date_demande = models.DateTimeField(verbose_name="Date de demande d'approvisionnement", auto_now_add=True, null=True, blank=True)
    date_confirmation = models.DateTimeField(verbose_name="Date de confirmation de l'approvisionnement", null=True, blank=True)
    quantite=models.PositiveIntegerField(verbose_name="Quantite",default=0,blank=True)
    titre=models.fields.CharField(max_length=255,verbose_name="Titre de l'approvisionnement")
    produit=models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True,blank=True,related_name='approvisionnements',verbose_name='Produit')
    fournisseur=models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True,blank=True,related_name='approvisionnements',verbose_name='Fournisseur')
    etat=models.BooleanField(default=False, null=True, blank=True,)
    def __str__(self):
        return f'{self.titre+""+self.date+""+self.quantite}'
    
class Promotion(models.Model):
    date_debut = models.DateField(verbose_name="Date de debut de la promotion", null=False)
    date_fin= models.DateField(verbose_name="Date de debut de la promotion")
    pourcentage=models.fields.DecimalField(max_digits=5,decimal_places=2, verbose_name="Pourcentage de reductions",validators=[MaxValueValidator(100.00, message="Le pourcentage doit être inférieur ou égal à 100."),MinValueValidator(0.01, message="Le pourcentage doit être supérieur ou égal à 0.01."),])
    description=models.fields.TextField(verbose_name="Description de la promotion")
    produits=models.ManyToManyField(Produit,related_name='promotions', blank=False)

    def __str__(self):
        return f'{self.pourcentage+""+self.date_debut.strftime+""+self.date_debut.strftime}'
    def clean(self):
        if self.date_debut is not None :
            if self.date_debut > self.date_fin:
                raise ValidationError("La date de début ne peut pas être supérieure à la date de fin.")

class AlerteRupture(models.Model):
    contenu=models.CharField(max_length=255, verbose_name='contenu')
    etat=models.BooleanField(default=False, verbose_name='etat')

