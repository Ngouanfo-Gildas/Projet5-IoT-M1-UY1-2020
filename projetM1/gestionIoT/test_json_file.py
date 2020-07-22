
import json
import os, sys, stat
import shutil

#print(os.getcwd())
#print(os.listdir('.'))

path = os.chdir("gestionIoT/donnee/")

def repertoire_p(id_p):
    """ Créer un repertoire pour chaque proprietaire
        id_p: identifiant du proprietaire
    """
    #os.chdir("gestionIoT/donnee/")
    dir_name = "propietaire_" + str(id_p)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        pass

def repertoire_r(id_p, id_r):
    """ créer un repertoire pour chaque réseau du proprietaire
        id_p: identifiant du proprietaire
        id_r: identifiat du réseau
    """
    # rep_p: repertoire proprietaire courant
    rep_p = "propietaire_" + str(id_p)
    os.chdir(rep_p)
    dir_name = "reseau_" + str(id_p )+ "_" + str(id_r)
    poubelle = "poubelle"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        os.chdir(dir_name)
        if not os.path.exists(poubelle):
            os.mkdir(poubelle)
            os.chdir("..")
        else:
            pass
    else:
        pass
    # on revient dans le repertoire parent de proprietaire
    os.chdir("..")

print(os.getcwd())
def lecture(id_p, id_r):
    """user = User()
    if user.is_authenticated:
        id_p = Proprietaire.objects.filter(user_id = request.user.id)
        id_r = Reseau.objects.filter(proprietaire_id = request.user.id)"""
        
    path_rep_r = "propietaire_" + str(id_p) + "/" + "reseau_" + str(id_p )+ "_" + str(id_r)
    os.chdir(path_rep_r)
    liste_fich = [fich for fich in os.listdir(".") if os.path.isfile(fich)]
    nbre_fich = len(liste_fich) #nombre de fichier reçu par le reseau id_r
    while nbre_fich != 0:
        for fjson in liste_fich:
            with open(fjson, 'r') as fich_json:
                data = json.load(fich_json)
                #print(data)
                datat = json.dumps(data, indent=3)
                print(datat)
            shutil.move(fjson, "poubelle/")
            liste_fich.remove(fjson)

#os.chmod('./data.json', stat.S_IRUSR)
lecture(5, 1) 






















path = os.chdir("gestionIoT/donnee/")

def repertoire_p(id_p):
    """ Créer un repertoire pour chaque proprietaire
        id_p: identifiant du proprietaire
    """
    #os.chdir("gestionIoT/donnee/")
    dir_name = "propietaire_" + str(id_p)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        pass


def repertoire_r(id_p, id_r):
    """ créer un repertoire pour chaque réseau du proprietaire
        id_p: identifiant du proprietaire
        id_r: identifiat du réseau
    """
    # rep_p: repertoire proprietaire courant
    rep_p = "propietaire_" + str(id_p)
    os.chdir(rep_p)
    dir_name = "reseau_" + str(id_p )+ "_" + str(id_r)
    poubelle = "poubelle"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        os.chdir(dir_name)
        if not os.path.exists(poubelle):
            os.mkdir(poubelle)
            os.chdir("..")
        else:
            pass
    else:
        pass
    # on revient dans le repertoire parent de proprietaire
    os.chdir("..")


def lecture(id_p, id_r):
    user = User()
    """if user.is_authenticated:
        id_p = Proprietaire.objects.filter(user_id = request.user.id)
        id_r = Reseau.objects.filter(proprietaire_id = request.user.id)"""
        
        path_rep_r = "propietaire_" + str(id_p) + "/" + "reseau_" + "_" + str(id_p )+ "_" + str(id_r)
        os.chdir(path_rep_r)
        liste_fich = [fich for fich in os.listdir(".") if os.path.isfile(fich)]
        nbre_fich = len(liste_fich) #nombre de fichier reçu par le reseau id_r
        while nbre_fich != 0:
            for fjson in liste_fich:
                with open(fjson, 'r') as fich_json:
                    data = json.load(fich_json)
                    #print(data)
                    datat = json.dumps(data, indent=3)
                    print(datat)

os.chmod('./data.json', stat.S_IRUSR)
lecture(5, 1) 
 