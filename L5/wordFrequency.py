# Scrie o functie word_frequency care primeste un sir de caractere si returneza un dictionar ce contine frecventa fiecarui cuvant din text.
# Ignora majusculele si semnele de punctuatie.

def word_frequency(text):
    # Convertim textul la litere mici
    text = text.lower()

    # Inlaturam semnele de punctuatie
    semne_punctuatie = ".,!?;:-"
    for semn in semne_punctuatie:
        text = text.replace(semn, "")

    # Impartim textul in cuvinte
    cuvinte = text.split()

    # Cream dictionarul cu frecventele
    frecventa = {}
    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] = frecventa[cuvant] + 1
        else:
            frecventa[cuvant] = 1

    return frecventa

# Testare
try:
    text_input = input("Introdu un text: ")

    if text_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        rezultat = word_frequency(text_input)
        print("Frecventa cuvintelor:", rezultat)

except Exception:
    print("Eroare! A aparut o problema la procesare.")
