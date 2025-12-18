# Scrie un program ce primeste a input o lista de numere separate de virgula,
# inlatura duplicatele si afiseaza lista cu valori unice in aceeasi ordine in care au aparut prima data.

try:
    lista_input = input("Introdu o lista de numere separate de virgula: ")

    if lista_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        # Convertim input-ul intr-o lista de numere intregi
        numere_text = lista_input.split(",")
        lista_numere = []

        for numar_text in numere_text:
            numar = int(numar_text)
            lista_numere.append(numar)

        print("Lista originala:", lista_numere)

        # Inlaturam duplicatele pastrand ordinea
        lista_unica = []
        for numar in lista_numere:
            if numar not in lista_unica:
                lista_unica.append(numar)

        print("Lista fara duplicate:", lista_unica)

except ValueError:
    print("Eroare! Te rog introdu doar numere separate de virgula.")
