import json
import sys
import hashlib

def chiffrement(message, décalage):
    nouveaumessage= ""
    for i in message:
        aski = ord(i) + décalage
        nouveaumessage += chr (aski)     
    return nouveaumessage

def afficher(listedessecrets):
    for secret in listedessecrets:
        print(chiffrement(secret, -13))


def ajouter(listedessecrets, secret):
    listedessecrets.append(chiffrement(secret, 13))

#charger sauvegarde
def loadfile():
    try:           #NOM DU FICHIER
        with open("Savy.json", "r") as f:
            data = json.load(f)
    except Exception: 
        data = {
        "bonmotdepasse": hashlib.sha512("AAA".encode()).hexdigest(),
        "secrets": []}
        saver(data)
    return data
def saver(data):

    with open('Savy.json', 'w') as f:

        json.dump(data, f)

data = loadfile()

loadfile()

while True:
    select= input("Que voulez vous faire? (Entrez a pour entrer et b pour quitter.)")

    if select== "a":
        motdepasse= input("Veuillez entrer le mot de passe.")
        motdepasse= hashlib.sha512(motdepasse.encode()).hexdigest()           
        if motdepasse== data ["bonmotdepasse"]:
            print("mot de passe correct!")   

 

            while True:
                
                message= input("Que voulez vous faire? (options: ajouter, afficher, effacer, sauvegarder et quitter, changer mot de passe)")
                if message== "déconnecter":
                    break
                if message== "ajouter":
                    secret= input("quel secret veux tu déposer?")
                    ajouter(data ["secrets"], secret)
                if message== "afficher":
                    input("Vos secrets sont...(appuyez sur entrée)")
                    afficher(data ["secrets"])
                if message== "effacer":
                    print("secrets effacés.")
                    data["secrets"] = []
                if message== "sauvegarder et quitter":
                    saver(data)
                    print("ok")                
                    sys.exit()
                if message== "changer mot de passe":
                    data ["bonmotdepasse"] = input("Veuillez entrer le nouveau mot de passe.")
                    print(f"voici votre nouveau mot de passe: {data ["bonmotdepasse"]}")
                    data ["bonmotdepasse"] = hashlib.sha512(data ["bonmotdepasse"].encode()).hexdigest()      

                    saver(data)


        else: 
            print("mot de passe incorrect")
    
    elif select== "b":
        print("ok :)")                
        sys.exit()

