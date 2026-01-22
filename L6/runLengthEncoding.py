#Problema 3: Scrie o functie run_length_encoding care primeste un sir de caractere si
#returneaza o versiune comprimata a sirului folosind codificarea tip Run-Length Encoding (RLE).
#Aceasta inlocuieste grupurile consecutive de caractere identice cu caracterul si
#numarul de aparitii consecutive.
#Ex: text = "aaabbbbcccdde" output: "a3b4c3d2e1"

try:
    text_input = input("Introdu un text pentru comprimare RLE: ")

    if text_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        result = ""
        count = 1

        #Parcurge textul si numara caracterele consecutive
        for i in range(len(text_input)):
            #Daca nu suntem la ultimul caracter si caracterul curent este la fel ca urmatorul
            if i < len(text_input) - 1 and text_input[i] == text_input[i + 1]:
                count = count + 1
            else:
                #Adauga caracterul si numarul de aparitii la rezultat
                result = result + text_input[i] + str(count)
                count = 1

        print("Textul comprimat:", result)

except Exception as e:
    print("Eroare! A aparut o problema:", e)
