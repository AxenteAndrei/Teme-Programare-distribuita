# Creeaza un program care cere userului un numar intreg si afiseaza daca acest numar este par sau impar.(hint, '%' returneaza restul impartirii)

numar = int(input("Introdu un numar intreg: "))

if numar % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
