#Problema 1: Importarea modulelor si utilizarea acestora
#Descriere:
#Creeaza un script Python care foloseste modulul math pentru a calcula:
#1. Radacina patrata a unui numar dat.
#2. Factorialul unui numar intreg.
#3. Valoarea sinusului unui unghi dat in grade.
#Input: num = 25 angle = 30
#Output:
#Radacina patrata a 25 este 5.0
#Factorialul lui 25 este 15511210043330985984000000
#Sinusul unghiului de 30 grade este 0.5

import math

try:
    num_input = input("Introdu un numar pentru calcule: ")

    if num_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        num = int(num_input)

        if num < 0:
            print("Eroare! Numarul trebuie sa fie pozitiv.")
        else:
            #1. Calculeaza radacina patrata
            sqrt_result = math.sqrt(num)
            print("Radacina patrata a", num, "este", sqrt_result)

            #2. Calculeaza factorialul
            factorial_result = math.factorial(num)
            print("Factorialul lui", num, "este", factorial_result)

            #3. Calculeaza sinusul unui unghi in grade
            angle_input = input("Introdu un unghi in grade pentru sinus: ")

            if angle_input == "":
                print("Eroare! Nu ai introdus nimic.")
            else:
                angle = float(angle_input)

                #Converteste grade in radiani
                angle_radians = math.radians(angle)

                #Calculeaza sinusul
                sin_result = math.sin(angle_radians)
                print("Sinusul unghiului de", angle, "grade este", sin_result)

except ValueError:
    print("Eroare! Te rog introdu un numar valid.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
