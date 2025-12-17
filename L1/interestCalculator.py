# Scrie un program ce calculeaza dobanda. Programul va cere utilizatorului principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani. Formula:
# Interest = (Principal x Rate x Time)/100

try:
    principal_input = input("Introdu suma principala: ")
    rata_input = input("Introdu rata anuala a dobanzii (de ex. 5, 6, 10): ")
    timp_input = input("Introdu timpul in ani: ")

    if principal_input == "" or rata_input == "" or timp_input == "":
        print("Eroare! Nu ai introdus toate valorile.")
    else:
        principal = float(principal_input)
        rata = float(rata_input)
        timp = float(timp_input)

        dobanda = (principal * rata * timp) / 100

        print("Dobanda calculata este:", dobanda)

except ValueError:
    print("Eroare! Te rog introdu numere valide.")
