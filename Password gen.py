# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import time
import string


def generate_password(length=12):

    if length < 8:
        time.sleep(1)
        raise ValueError("le mot de passe doit être plus long que 8 caractères")





    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    
    ]

    all_chars = lower + upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)

    return ''.join(password)

assert len (generate_password (12)) == 12
assert len (generate_password (8)) == 8

if __name__ == "__main__":
    print ("=== Générateur de mot de passe sécurisé ===")
    try:
        user_length = int(input("entrer longueur souhaitée: "))
        pwd = generate_password(user_length)
        print("mot de passe généré:", pwd)
        
    except ValueError as ve:
        print("Erreur:", ve)
        time.sleep(3)
    

generate_password(length=12)
input("Appuyez sur Entrée pour quitter.") 