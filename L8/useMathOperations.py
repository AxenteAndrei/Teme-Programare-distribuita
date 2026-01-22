#Script care importa modulul mathOperations si foloseste functiile acestuia

import mathOperations

try:
    num1_input = input("Introdu primul numar: ")
    num2_input = input("Introdu al doilea numar: ")

    if num1_input == "" or num2_input == "":
        print("Eroare! Nu ai introdus numerele.")
    else:
        num1 = float(num1_input)
        num2 = float(num2_input)

        #Efectueaza operatiile folosind functiile din modul
        print("\nRezultate:")
        print("Adunare:", num1, "+", num2, "=", mathOperations.adunare(num1, num2))
        print("Scadere:", num1, "-", num2, "=", mathOperations.scadere(num1, num2))
        print("Inmultire:", num1, "*", num2, "=", mathOperations.inmultire(num1, num2))

        #Verifica impartirea la 0
        rezultat_impartire = mathOperations.impartire(num1, num2)
        if rezultat_impartire is None:
            print("Impartire: Eroare! Nu se poate imparti la 0.")
        else:
            print("Impartire:", num1, "/", num2, "=", rezultat_impartire)

except ValueError:
    print("Eroare! Te rog introdu numere valide.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
