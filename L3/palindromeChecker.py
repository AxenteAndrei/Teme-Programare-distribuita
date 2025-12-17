#Scrie o functie is_palindrome(word) ce verifica daca un cuvant dat este palindrom (se citeste la fel si de la stanga la dreapta, dar si de la dreapta la stanga).
#Functia trebuie sa returneze True cand cuvantul dat este palindrom si False cand nu este palindrom.
#Folositi functia definita intr-un program ce preia de la tastatura un cuvant dat si il verifica.

def is_palindrome(word):
    word = word.lower()
    word_inversat = word[::-1]

    if word == word_inversat:
        return True
    else:
        return False

cuvant = input("Introdu un cuvant: ")

if cuvant == "":
    print("Eroare! Nu ai introdus nimic.")
else:
    if is_palindrome(cuvant):
        print("Cuvantul este palindrom!")
    else:
        print("Cuvantul nu este palindrom.")
