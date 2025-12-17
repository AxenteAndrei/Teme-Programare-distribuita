#Scrie o functie distance(x1, y1, x2, y2) ce calculeaza distanta euclideana intre doua puncte (x1, y1) si (x2, y2).
#Foloseste aceasta functie intr-un program care cere coordonatele a doua puncte si printeaza distanta intre ele.

import math

def distance(x1, y1, x2, y2):
    distanta = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distanta

try:
    print("Introdu coordonatele primului punct:")
    x1_input = input("x1: ")
    y1_input = input("y1: ")

    print("Introdu coordonatele celui de-al doilea punct:")
    x2_input = input("x2: ")
    y2_input = input("y2: ")

    if x1_input == "" or y1_input == "" or x2_input == "" or y2_input == "":
        print("Eroare! Nu ai introdus toate valorile.")
    else:
        x1 = float(x1_input)
        y1 = float(y1_input)
        x2 = float(x2_input)
        y2 = float(y2_input)

        distanta_calculata = distance(x1, y1, x2, y2)

        print("Distanta intre punctele (", x1, ",", y1, ") si (", x2, ",", y2, ") este:", distanta_calculata)

except ValueError:
    print("Eroare! Te rog introdu numere valide.")
