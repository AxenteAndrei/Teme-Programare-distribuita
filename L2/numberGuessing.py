#Creaza un joc simplu de ghicit un numar, unde programul alege un numar aleator intre 1 si 20.
#Utilizatorul are 5 incercari pentru a ghici numarul.
#Dupa fiecare incercare, programul va oferi feedback ("Prea mare", "Prea mic", sau "Corect!")

import random

numar_secret = random.randint(1, 20)
incercari_ramase = 5

print("Bine ai venit la jocul de ghicit numere!")
print("Am ales un numar intre 1 si 20. Ai 5 incercari sa-l ghicesti!")

while incercari_ramase > 0:
    try:
        ghicit_input = input("Introdu numarul tau: ")

        if ghicit_input == "":
            print("Eroare! Nu ai introdus nimic.")
            continue

        ghicit = int(ghicit_input)

        if ghicit < 1 or ghicit > 20:
            print("Te rog introdu un numar intre 1 si 20!")
            continue

        if ghicit == numar_secret:
            print("Corect! Ai ghicit numarul!")
            break
        elif ghicit > numar_secret:
            print("Prea mare!")
        else:
            print("Prea mic!")

        incercari_ramase = incercari_ramase - 1

        if incercari_ramase > 0:
            print("Mai ai", incercari_ramase, "incercari.")
        else:
            print("Ai pierdut! Numarul era", numar_secret)

    except ValueError:
        print("Eroare! Te rog introdu un numar valid.")
