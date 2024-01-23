# Generated by Django 5.0.1 on 2024-01-10 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_categorie_client_produit_vente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approvisionnnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, verbose_name='Date de vente')),
                ('quantite', models.PositiveIntegerField(blank=True, default=0, verbose_name='Quantite')),
                ('titre', models.CharField(max_length=255, verbose_name="Titre de l'approvisionnement")),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approvisionnements', to='market.produit', verbose_name='Produit')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=255, verbose_name='Prénom')),
                ('telephone', models.CharField(max_length=8, verbose_name='Telephone')),
                ('adresse', models.CharField(max_length=255, verbose_name='Adresse')),
                ('produits', models.ManyToManyField(related_name='fournisseurs', through='market.Approvisionnnement', to='market.produit')),
            ],
        ),
        migrations.AddField(
            model_name='approvisionnnement',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approvisionnements', to='market.fournisseur', verbose_name='Fournisseur'),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_fin', models.DateField(auto_created=True, verbose_name='Date de debut de la promotion')),
                ('date_debut', models.DateField(auto_created=True, verbose_name='Date de debut de la promotion')),
                ('pourcentage', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Pourcentage de reductions')),
                ('description', models.TextField(verbose_name='Description de la promotion')),
                ('produits', models.ManyToManyField(related_name='promotions', to='market.produit')),
            ],
        ),
    ]