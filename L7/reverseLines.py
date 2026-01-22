#Problema 2: Scrie o functie reverse_lines care citeste continutul unui fisier si creaza
#un alt fisier unde fiecare rand este scris invers (caracterele din rand sunt inversate).
#Ex:
#Fisierul input.txt contine:
#Python este grozav.
#Imi place sa lucrez cu fisiere.
#Fisierul output.txt va contine:
#.vazorg etse nohtyP
#.ereisif uc zercul as ecalp imI

try:
    input_file_name = input("Introdu numele fisierului de input: ")
    output_file_name = input("Introdu numele fisierului de output: ")

    if input_file_name == "" or output_file_name == "":
        print("Eroare! Nu ai introdus numele fisierelor.")
    else:
        #Deschide fisierul de input pentru citire
        file_in = open(input_file_name, "r", encoding="utf-8")

        #Citeste toate liniile din fisier
        lines = file_in.readlines()

        #Inchide fisierul de input
        file_in.close()

        #Deschide fisierul de output pentru scriere
        file_out = open(output_file_name, "w", encoding="utf-8")

        #Proceseaza fiecare linie
        for line in lines:
            #Elimina caracterul newline de la final
            line_clean = line.rstrip("\n")

            #Inverseaza linia
            line_reversed = line_clean[::-1]

            #Scrie linia inversata in fisierul de output
            file_out.write(line_reversed + "\n")

        #Inchide fisierul de output
        file_out.close()

        print("Fisierul a fost procesat cu succes!")

except FileNotFoundError:
    print("Eroare! Fisierul de input nu a fost gasit.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
