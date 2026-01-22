#Problema 1: Scrie o functie count_words_in_file care citeste continutul unui fisier text
#si returneaza numarul total de cuvinte din fisier.
#Ex: fisierul example.txt contine:
#Salut tuturor. Aceasta este o demonstratie de lucru cu fisiere.
#Output: 12

try:
    file_name_input = input("Introdu numele fisierului: ")

    if file_name_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        #Deschide fisierul pentru citire
        file = open(file_name_input, "r", encoding="utf-8")

        #Citeste tot continutul fisierului
        content = file.read()

        #Inchide fisierul
        file.close()

        #Imparte continutul in cuvinte si numara-le
        words = content.split()
        word_count = len(words)

        print("Numarul total de cuvinte:", word_count)

except FileNotFoundError:
    print("Eroare! Fisierul nu a fost gasit.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
