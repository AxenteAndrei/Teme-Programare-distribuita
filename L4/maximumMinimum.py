# Scrie un program care cere de la tastatura o lista de numere separate de virgula.
# Programul trebuie sa converteasca inputul intr-o lista de numere intregi si sa afiseze maximul si minimul din lista.

try:
    lista_input = input("Introdu o lista de numere separate de virgula: ")

    if lista_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        # Convertim input-ul intr-o lista de numere intregi
        lista_numere = []
        numere_text = lista_input.split(",")

        for numar_text in numere_text:
            numar = int(numar_text)
            lista_numere.append(numar)

        # Gasim maximul si minimul
        maxim = max(lista_numere)
        minim = min(lista_numere)

        print("Lista de numere:", lista_numere)
        print("Maximul este:", maxim)
        print("Minimul este:", minim)

except ValueError:
    print("Eroare! Te rog introdu doar numere separate de virgula.")
