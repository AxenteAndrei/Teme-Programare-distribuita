# Faceti un program care verifică dacă un numar introdus de utilizator e prim sau nu.

numar = int(input("Introdu un numar intreg: "))

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
