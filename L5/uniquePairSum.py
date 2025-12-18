# Scrie o functie unique_pair_sum care primeste o lista de numere intregi si o valoare tinta.
# Functia returneza o multime de perechi unice de numere care adunate dau valoarea tinta.
# Fiecare pereche trebuie sa fie reprezentata ca un tuplu (a, b) unde a <= b.

def unique_pair_sum(numbers, target):
    # Cream o multime pentru a pastra perechi unice
    perechi = set()

    # Parcurgem toate combinatiile posibile
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Verificam daca suma celor doua numere este egala cu target
            if numbers[i] + numbers[j] == target:
                # Cream perechea cu numarul mic primul
                if numbers[i] <= numbers[j]:
                    pereche = (numbers[i], numbers[j])
                else:
                    pereche = (numbers[j], numbers[i])

                perechi.add(pereche)

    return perechi

# Testare
try:
    lista_input = input("Introdu o lista de numere separate de virgula: ")

    if lista_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        # Convertim input-ul intr-o lista de numere
        numere_text = lista_input.split(",")
        numere = []
        for numar_text in numere_text:
            numar = int(numar_text)
            numere.append(numar)

        target_input = input("Introdu valoarea tinta: ")

        if target_input == "":
            print("Eroare! Nu ai introdus nimic.")
        else:
            target = int(target_input)

            rezultat = unique_pair_sum(numere, target)
            print("Perechi unice cu suma", target, ":", rezultat)

except ValueError:
    print("Eroare! Te rog introdu doar numere valide.")
