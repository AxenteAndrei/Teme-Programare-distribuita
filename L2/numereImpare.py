#Scrie un program care citeste un nr n de la tastatura si afiseaza toate numerele impare pana la n.
#ex: n = 10
#rezultat: 1, 3, 5, 7, 9

try:
    n_input = input("Introdu numarul n: ")

    if n_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        n = int(n_input)

        if n < 1:
            print("Te rog introdu un numar mai mare decat 0.")
        else:
            print("Numerele impare pana la", n, "sunt:")

            for i in range(1, n + 1):
                if i % 2 == 1:
                    print(i, end=", ")

            print()

except ValueError:
    print("Eroare! Te rog introdu un numar intreg valid.")
