# Scrie o functie inverted_index care primeste o lista de siruri de caractere (fiecare sir reprezentand un document)
# si returneza un dictionar. Dictionarul trebuie sa asocieze fiecarui cuvant unic un set de indici ai documentelor in care apare acel cuvant.

def inverted_index(documents):
    # Cream dictionarul
    index = {}

    # Parcurgem fiecare document
    for i in range(len(documents)):
        document = documents[i]

        # Convertim la litere mici si impartim in cuvinte
        document = document.lower()
        cuvinte = document.split()

        # Pentru fiecare cuvant, adaugam indexul documentului
        for cuvant in cuvinte:
            if cuvant in index:
                index[cuvant].add(i)
            else:
                index[cuvant] = {i}

    return index

# Testare
try:
    print("Introdu documentele (un document pe linie). Scrie 'gata' pentru a termina.")

    documents = []
    while True:
        document_input = input("Document: ")

        if document_input == "gata":
            break

        if document_input == "":
            print("Document gol, il sar.")
        else:
            documents.append(document_input)

    if len(documents) == 0:
        print("Nu ai introdus niciun document.")
    else:
        rezultat = inverted_index(documents)
        print("Indexul inversat:", rezultat)

except Exception:
    print("Eroare! A aparut o problema la procesare.")
