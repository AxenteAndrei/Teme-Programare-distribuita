#Problema 2: Gestionarea angajatilor (Inheritance, Creating Subclasses, Overriding Methods)
#Descriere: Creeaza o clasa de baza Employee care sa contina:
#- Atribute: name, salary.
#- Metoda: get_details(), care returneaza detalii despre angajat.
#Creeaza o subclasa Manager care mosteneste Employee si adauga:
#- Atributul suplimentar department.
#- Suprascrie metoda get_details() pentru a include departamentul.
#Exemplu:
#emp = Employee("John", 3000)
#mgr = Manager("Alice", 5000, "IT")
#print(emp.get_details()) # "Employee: John, Salary: 3000"
#print(mgr.get_details()) # "Manager: Alice, Salary: 5000, Department: IT"

class Employee:
    def __init__(self, name, salary):
        #Atribute pentru angajat
        self.name = name
        self.salary = salary

    def get_details(self):
        #Returneaza detaliile angajatului
        return "Employee: " + self.name + ", Salary: " + str(self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        #Apeleaza constructorul clasei parinte
        Employee.__init__(self, name, salary)
        #Adauga atributul department
        self.department = department

    def get_details(self):
        #Suprascrie metoda pentru a include departamentul
        return "Manager: " + self.name + ", Salary: " + str(self.salary) + ", Department: " + self.department

#Program principal
try:
    print("=== Sistem de Gestionare Angajati ===")
    print("\n1. Adauga angajat simplu")
    print("2. Adauga manager")

    choice = input("Alege o optiune: ")

    if choice == "1":
        #Creeaza un angajat simplu
        name_input = input("Introdu numele angajatului: ")
        salary_input = input("Introdu salariul: ")

        if name_input == "" or salary_input == "":
            print("Eroare! Nu ai introdus toate datele.")
        else:
            salary = float(salary_input)

            if salary < 0:
                print("Eroare! Salariul nu poate fi negativ.")
            else:
                emp = Employee(name_input, salary)
                print("\nAngajat creat:")
                print(emp.get_details())

    elif choice == "2":
        #Creeaza un manager
        name_input = input("Introdu numele managerului: ")
        salary_input = input("Introdu salariul: ")
        department_input = input("Introdu departamentul: ")

        if name_input == "" or salary_input == "" or department_input == "":
            print("Eroare! Nu ai introdus toate datele.")
        else:
            salary = float(salary_input)

            if salary < 0:
                print("Eroare! Salariul nu poate fi negativ.")
            else:
                mgr = Manager(name_input, salary, department_input)
                print("\nManager creat:")
                print(mgr.get_details())

    else:
        print("Optiune invalida!")

except ValueError:
    print("Eroare! Te rog introdu valori numerice valide pentru salariu.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
