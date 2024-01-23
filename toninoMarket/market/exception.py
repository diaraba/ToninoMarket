from market.models import Categorie, Produit


def get_produit_by_categorie_id(categorie_id):
    try:
        categorie = Categorie.objects.get(id=categorie_id)

        produit = Produit.objects.get(categorie=categorie)

        return produit
    except Produit.DoesNotExist:
        return None
