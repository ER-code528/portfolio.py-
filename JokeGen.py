
"""
Created on Fri Feb 20 18:03:47 2026

@author: firec
"""
import time
from random import randint
def program_joker():
    print("Que voulez vous faire?")

    print("1: blague")
    ye = int(input("2: sortir       "))

    if ye == 2 :
        exit()
    elif ye == 1:
        joke = randint(1,11)
        if joke == 1:
            print("Pourquoi le squelette n'a t'il pas d'amis?")
            time.sleep(2.5)
            print("Parce qu'il n'OS pas parler aux autres!") 
        elif joke == 2:
            print("Pourquoi le poulet a t il traversé la route?")  
            time.sleep(2.5)
            print("Je ne sais pas.")  

        elif joke == 3:
            print("T'as entendu parler de la blague de l'oeuf?")  
            time.sleep(2.5)
            print("Elle m'a fait craquer de rire!")
        elif joke == 4:
            print("Qu'est ce qu'un rat qui fait la vaisselle?")  
            time.sleep(2.5)
            print("Un raton laveur!")
        elif joke == 5:
            print("Qu'est ce qu'un rat qui a perdu sa queue?")  
            time.sleep(2.5)
            print("Un raccourci!")
        elif joke == 6:
            print("Pourquoi le squelette n'a t'il pas d'amis?")
            time.sleep(2.5)
            print("Parce qu'il n'OS pas parler aux autres!") 
        elif joke == 7:
            print("Pourquoi le poulet a t il traversé la route?")  
            time.sleep(2.5)
            print("Je ne sais pas.")  

        elif joke == 8:
            print("T'as entendu parler de la blague de l'oeuf?")  
            time.sleep(2.5)
            print("Elle m'a fait craquer de rire!")
        elif joke == 9:
            print("Qu'est ce qu'un rat qui fait la vaisselle?")  
            time.sleep(2.5)
            print("Un raton laveur!")
        elif joke == 10:
            print("Qu'est ce qu'un rat qui a perdu sa queue?")  
            time.sleep(2.5)
            print("Un raccourci!")
        elif joke == 11:
            print("Qu'est ce qu'un")
            time.sleep(0.97)
            print("Euh")
            time.sleep(0.7)
            print("Un")
            time.sleep(0.9)
            print("Euh")
            time.sleep(0.3)
            print("Attends")
            time.sleep(0.4)
            print("Attends")
            time.sleep(0.4)
            print("Attends")
            time.sleep(1.4)
            print("J'ai oublié ma blague.")
            time.sleep(0.51)
        time.sleep(2.3)
        program_joker()


program_joker()