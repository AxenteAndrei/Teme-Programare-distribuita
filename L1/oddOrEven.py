# Creeaza un program care cere userului un numar intreg si afiseaza daca acest numar este par sau impar.(hint, '%' returneaza restul impartirii)

try:
    numar_input = input("Introdu un numar intreg: ")

    if numar_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        numar = int(numar_input)

        if numar % 2 == 0:
            print("Numarul este par")
        else:
            print("Numarul este impar")

except ValueError:
    print("Eroare! Te rog introdu un numar intreg valid.")
