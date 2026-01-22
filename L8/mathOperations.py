#Problema 2: Scrierea scripturilor Python ca module
#Descriere:
#Scrie un script Python numit math_operations.py care contine functii pentru urmatoarele operatii:
#1. Adunare
#2. Scadere
#3. Inmultire
#4. Impartire

def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        return None
    return a / b
