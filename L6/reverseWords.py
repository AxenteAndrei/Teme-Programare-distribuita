#Problema 1: Scrie o functie reverse_words care primeste o propozitie (un sir de caractere) si
#returneaza o propozitie noua in care ordinea cuvintelor este inversata, dar ordinea literelor in
#fiecare cuvant ramane aceeasi. Elimina spatiile suplimentare din propozitie daca exista.
#Ex: sentence = "soricel un cu joaca se pisica", OUTPUT: "pisica se joaca cu un soricel"

try:
    sentence_input = input("Introdu o propozitie: ")

    if sentence_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        #Imparte propozitia in cuvinte (elimina automat spatiile multiple)
        words = sentence_input.split()

        #Inverseaza ordinea cuvintelor
        reversed_words = words[::-1]

        #Uneste cuvintele inapoi intr-o propozitie
        result = " ".join(reversed_words)

        print("Propozitia inversata:", result)

except Exception as e:
    print("Eroare! A aparut o problema:", e)
