# Scrie un program ce calculeaza dobanda. Programul va cere utilizatorului principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani. Formula:
# Interest = (Principal x Rate x Time)/100

principal = float(input("Introdu suma principala: "))
rata = float(input("Introdu rata anuala a dobanzii (de ex. 5, 6, 10): "))
timp = float(input("Introdu timpul in ani: "))

dobanda = (principal * rata * timp) / 100

print("Dobanda calculata este:", dobanda)
