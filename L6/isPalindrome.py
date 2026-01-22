#Problema 2: Scrie o functie is_palindrome care primeste un sir de caractere si verifica daca
#este un palindrom, ignorand literele mari si spatiile. Un sir este un palindrom daca este
#identic atunci cand este citit de la stanga la dreapta si de la dreapta la stanga.
#Ex: text = "A man a plan a canal Panama", output: True

try:
    text_input = input("Introdu un text pentru a verifica daca este palindrom: ")

    if text_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        #Transforma textul in litere mici
        text_lower = text_input.lower()

        #Elimina toate spatiile
        text_clean = text_lower.replace(" ", "")

        #Inverseaza textul
        text_reversed = text_clean[::-1]

        #Verifica daca textul este identic cu inversul sau
        if text_clean == text_reversed:
            print("Textul este un palindrom!")
        else:
            print("Textul nu este un palindrom.")

except Exception as e:
    print("Eroare! A aparut o problema:", e)
