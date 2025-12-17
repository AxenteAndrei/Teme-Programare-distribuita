# Faceti un program care verifică dacă un numar introdus de utilizator e prim sau nu.

try:
    numar_input = input("Introdu un numar intreg: ")

    if numar_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        numar = int(numar_input)

        if numar <= 1:
            print("Numarul nu este prim")
        else:
            este_prim = True
            for i in range(2, numar):
                if numar % i == 0:
                    este_prim = False
                    break

            if este_prim:
                print("Numarul este prim")
            else:
                print("Numarul nu este prim")

except ValueError:
    print("Eroare! Te rog introdu un numar intreg valid.")
