from getpass import *

mot = getpass("entrez un mot : ")

liste = []

liste2 = []

for x in mot :
    liste.append(x)
    liste2.append('*')

print ("".join(liste2))

nb_err=0

while nb_err < 9 :
    lettre = input("Entrez votre lettre :")

    if len(lettre)> 1 :
        if lettre == mot :
            print("Vous avez gagné !")
            break
    if lettre in liste :
        for(index,y) in enumerate(liste):
            if y == lettre:
                liste2[index] = y


        v = ("".join(liste2))
        print("Vous avez trouvé une lettre : ", v)
        if liste == liste2 :
            print ("Vous avez gagné : ")
            break
    else:
        nb_err+=1
        print("Mauvaise réponse, il vous reste %s essais"%(9-nb_err))
        if nb_err>=9:
            print(" ============ ")
        if nb_err>=8:
            print(" ============ ")
        if nb_err>=7:
            print(" ||/      |   ")
        if nb_err>6:
            print(" ||/      |   ")
        if nb_err>=5:
            print(" ||/      O   ")
        if nb_err>=4:
            print(" ||      /|\  ")
        if nb_err>=3:
            print(" ||/      /\  ")
        if nb_err>=2:
            print(" ||/          ")
        if nb_err>=1:
            print("==============\n")

if nb_err == 9:
    print("Vous avez perdu, le mot était : ", mot)
        




























        
