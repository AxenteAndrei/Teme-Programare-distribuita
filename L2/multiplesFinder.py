#Scrie un program care cere utilizatorului sa introduca doua numere, x si y, si afiseaza toate multiplurile lui x care sunt mai mici decat y.

try:
    x_input = input("Introdu numarul x: ")
    y_input = input("Introdu numarul y: ")

    if x_input == "" or y_input == "":
        print("Eroare! Nu ai introdus toate valorile.")
    else:
        x = int(x_input)
        y = int(y_input)

        if x == 0:
            print("Eroare! Numarul x nu poate fi 0.")
        else:
            print("Multiplurile lui", x, "mai mici decat", y, "sunt:")

            multiplu = x
            while multiplu < y:
                print(multiplu)
                multiplu = multiplu + x

except ValueError:
    print("Eroare! Te rog introdu numere intregi valide.")
