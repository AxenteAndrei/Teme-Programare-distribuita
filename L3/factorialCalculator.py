#Scrie o functie factorial(n) care calculeaza factorialul unui numar n.
#Folositi aceasta functie intr-un program care cere de la tastatura un numar intreg si returneaza factorialul acestuia.

def factorial(n):
    if n == 0 or n == 1:
        return 1

    rezultat = 1
    for i in range(2, n + 1):
        rezultat = rezultat * i

    return rezultat

try:
    numar_input = input("Introdu un numar intreg: ")

    if numar_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        numar = int(numar_input)

        if numar < 0:
            print("Eroare! Factorialul nu este definit pentru numere negative.")
        else:
            rezultat_factorial = factorial(numar)
            print("Factorialul lui", numar, "este:", rezultat_factorial)

except ValueError:
    print("Eroare! Te rog introdu un numar intreg valid.")
