#Problema 3: Forme geometrice (Polymorphism, Understanding Dunder Methods)
#Descriere:
#- Creeaza o clasa de baza Shape care sa contina metoda area() ce returneaza aria formei geometrice.
#- Creeaza doua clase care mostenesc Shape:
#  1. Circle - sa calculeze aria unui cerc.
#  2. Rectangle - sa calculeze aria unui dreptunghi.
#- Adauga metode dunder pentru afisare (__str__) in fiecare clasa pentru a oferi o
#  reprezentare textuala.
#Exemplu:
#circle = Circle(5)
#rectangle = Rectangle(10, 4)
#print(circle) # "Circle with radius 5 has area 78.54"
#print(rectangle) # "Rectangle with width 10 and height 4 has area 40"

import math

class Shape:
    def area(self):
        #Metoda de baza pentru aria
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        #Calculeaza aria cercului: π * r^2
        return math.pi * self.radius * self.radius

    def __str__(self):
        #Metoda dunder pentru afisare
        area_value = self.area()
        return "Circle with radius " + str(self.radius) + " has area " + str(round(area_value, 2))

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        #Calculeaza aria dreptunghiului: lungime * latime
        return self.width * self.height

    def __str__(self):
        #Metoda dunder pentru afisare
        area_value = self.area()
        return "Rectangle with width " + str(self.width) + " and height " + str(self.height) + " has area " + str(area_value)

#Program principal
try:
    print("=== Calculator Forme Geometrice ===")
    print("\n1. Cerc")
    print("2. Dreptunghi")

    choice = input("Alege o forma: ")

    if choice == "1":
        #Creeaza un cerc
        radius_input = input("Introdu raza cercului: ")

        if radius_input == "":
            print("Eroare! Nu ai introdus raza.")
        else:
            radius = float(radius_input)

            if radius < 0:
                print("Eroare! Raza nu poate fi negativa.")
            else:
                circle = Circle(radius)
                print(circle)

    elif choice == "2":
        #Creeaza un dreptunghi
        width_input = input("Introdu latimea dreptunghiului: ")
        height_input = input("Introdu inaltimea dreptunghiului: ")

        if width_input == "" or height_input == "":
            print("Eroare! Nu ai introdus dimensiunile.")
        else:
            width = float(width_input)
            height = float(height_input)

            if width < 0 or height < 0:
                print("Eroare! Dimensiunile nu pot fi negative.")
            else:
                rectangle = Rectangle(width, height)
                print(rectangle)

    else:
        print("Optiune invalida!")

except ValueError:
    print("Eroare! Te rog introdu valori numerice valide.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
