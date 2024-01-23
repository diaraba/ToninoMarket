from market.models import AlerteRupture


def is_gerant(user):
    if user.groups.filter(name='Gerant').exists():
        return True
    
#verifier si l'utilisateur connecter est un caissier
def is_caissier(user):
    return user.groups.filter(name='Caissier ').exists()


def base(request):
    global_alerte_ruptures=AlerteRupture.objects.all()
    alerte_ruptures=[]
    nombre=0
    for alerte_rupture in global_alerte_ruptures:
        if not alerte_rupture.etat:
            alerte_ruptures.append(alerte_rupture)
            nombre=nombre+1
    return {'nombre': nombre}
