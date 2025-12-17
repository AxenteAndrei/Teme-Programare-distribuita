#Scrie un program care cere utilizatorului input grade Celsius si le converteste in grade farenheit.
#Farenheit = Celsius x 9/5 + 32

try:
    celsius_input = input("Introdu temperatura in grade Celsius: ")

    if celsius_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        celsius = float(celsius_input)
        fahrenheit = celsius * 9/5 + 32
        print("Temperatura in Fahrenheit este:", fahrenheit)

except ValueError:
    print("Eroare! Te rog introdu un numar valid.")
