# Scrie un program care creeaza o tupla din inputul primit de la tastatura (valori separate prin virgula).
# Apoi, cere utilizatorului sa introduca o valoare care sa fie cautata in tupla.
# Printeaza daca valoarea se regaseste in tupla sau nu, iar daca da, printeaza indexul la care se gaseste aceasta.

try:
    tupla_input = input("Introdu valori separate prin virgula: ")

    if tupla_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        # Convertim input-ul intr-o lista si apoi intr-o tupla
        valori_text = tupla_input.split(",")
        valori_lista = []

        for valoare_text in valori_text:
            valoare = int(valoare_text)
            valori_lista.append(valoare)

        tupla = tuple(valori_lista)
        print("Tupla:", tupla)

        # Cerem valoarea de cautat
        search_input = input("Introdu valoarea pe care vrei sa o cauti: ")

        if search_input == "":
            print("Eroare! Nu ai introdus nimic.")
        else:
            search_value = int(search_input)

            # Cautam valoarea in tupla
            if search_value in tupla:
                index = tupla.index(search_value)
                print(search_value, "se regaseste in tupla la indexul", index)
            else:
                print(search_value, "nu se regaseste in tupla")

except ValueError:
    print("Eroare! Te rog introdu doar numere valide.")
