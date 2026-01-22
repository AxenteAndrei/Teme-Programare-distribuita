#Problema 3: Scrie o functie filter_lines care citeste continutul unui fisier si creaza
#un alt fisier care contine doar liniile ce includ un cuvant cheie specific.
#Fisierul input.txt contine:
#Python este un limbaj versatil.
#Java este popular in dezvoltarea enterprise.
#Python este folosit in stiinta datelor.
#Python este usor de invatat.
#Fisierul filtered.txt va contine:
#Python este un limbaj versatil.
#Python este folosit in stiinta datelor.
#Python este usor de invatat.

try:
    input_file_name = input("Introdu numele fisierului de input: ")
    output_file_name = input("Introdu numele fisierului de output: ")
    keyword_input = input("Introdu cuvantul cheie de cautat: ")

    if input_file_name == "" or output_file_name == "" or keyword_input == "":
        print("Eroare! Nu ai introdus toate informatiile necesare.")
    else:
        #Deschide fisierul de input pentru citire
        file_in = open(input_file_name, "r", encoding="utf-8")

        #Citeste toate liniile din fisier
        lines = file_in.readlines()

        #Inchide fisierul de input
        file_in.close()

        #Deschide fisierul de output pentru scriere
        file_out = open(output_file_name, "w", encoding="utf-8")

        #Filtreaza liniile care contin cuvantul cheie
        for line in lines:
            if keyword_input in line:
                file_out.write(line)

        #Inchide fisierul de output
        file_out.close()

        print("Fisierul a fost filtrat cu succes!")

except FileNotFoundError:
    print("Eroare! Fisierul de input nu a fost gasit.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
