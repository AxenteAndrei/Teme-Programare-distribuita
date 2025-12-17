#Scrie un program care cere utilizatorului sa introduca un scor procentual (0-100).
#Pe baza scorului, programul va afisa nota corespunzatoare folosind urmatoarele criterii:
#90 si peste: Nota A
#80 pana la 89: Nota B
#70 pana la 79: Nota C
#60 pana la 69: Nota D
#Sub 60: Nota F

try:
    scor_input = input("Introdu scorul procentual (0-100): ")

    if scor_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        scor = float(scor_input)

        if scor < 0 or scor > 100:
            print("Eroare! Scorul trebuie sa fie intre 0 si 100.")
        elif scor >= 90:
            print("Nota: A")
        elif scor >= 80:
            print("Nota: B")
        elif scor >= 70:
            print("Nota: C")
        elif scor >= 60:
            print("Nota: D")
        else:
            print("Nota: F")

except ValueError:
    print("Eroare! Te rog introdu un numar valid.")
