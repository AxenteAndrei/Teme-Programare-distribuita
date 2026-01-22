#Problema 3: Crearea si utilizarea pachetelor Python
#Descriere:
#Creeaza un pachet Python numit geometry care contine doua module:
#1. circle.py: functii pentru aria si circumferinta unui cerc.
#2. rectangle.py: functii pentru aria si perimetrul unui dreptunghi.
#Apoi creeaza un script principal care foloseste acest pachet.

from geometry import circle
from geometry import rectangle

print("=== Calculator Geometric ===")
print("\n1. Calcule pentru cerc")
print("2. Calcule pentru dreptunghi")

try:
    optiune = input("\nAlege o optiune (1 sau 2): ")

    if optiune == "":
        print("Eroare! Nu ai introdus nimic.")
    elif optiune == "1":
        #Calcule pentru cerc
        raza_input = input("Introdu raza cercului: ")

        if raza_input == "":
            print("Eroare! Nu ai introdus raza.")
        else:
            raza = float(raza_input)

            if raza < 0:
                print("Eroare! Raza trebuie sa fie pozitiva.")
            else:
                print("\nRezultate pentru cerc:")
                print("Aria:", circle.aria(raza))
                print("Circumferinta:", circle.circumferinta(raza))

    elif optiune == "2":
        #Calcule pentru dreptunghi
        lungime_input = input("Introdu lungimea dreptunghiului: ")
        latime_input = input("Introdu latimea dreptunghiului: ")

        if lungime_input == "" or latime_input == "":
            print("Eroare! Nu ai introdus dimensiunile.")
        else:
            lungime = float(lungime_input)
            latime = float(latime_input)

            if lungime < 0 or latime < 0:
                print("Eroare! Dimensiunile trebuie sa fie pozitive.")
            else:
                print("\nRezultate pentru dreptunghi:")
                print("Aria:", rectangle.aria(lungime, latime))
                print("Perimetrul:", rectangle.perimetru(lungime, latime))

    else:
        print("Optiune invalida! Alege 1 sau 2.")

except ValueError:
    print("Eroare! Te rog introdu valori numerice valide.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
