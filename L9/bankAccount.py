#Problema 1: Gestionarea conturilor bancare (Encapsulation, Instantiating, Adding Attributes and Methods)
#Descriere:
#Creeaza o clasa BankAccount care sa reprezinte un cont bancar. Utilizeaza encapsulation
#pentru a proteja soldul contului. Clasa ar trebui sa contina:
#- Un atribut privat _balance.
#- Metode publice pentru:
#  - Depunere (deposit(amount)): Adauga bani in cont.
#  - Retragere (withdraw(amount)): Retrage bani din cont, daca exista suficient sold.
#  - Obtinerea soldului (get_balance()).

class BankAccount:
    def __init__(self, initial_balance=0):
        #Atribut privat pentru sold (cu underscore)
        self._balance = initial_balance

    def deposit(self, amount):
        #Adauga bani in cont
        if amount > 0:
            self._balance = self._balance + amount
            print("Depunere reusita! Sold nou:", self._balance)
        else:
            print("Eroare! Suma trebuie sa fie pozitiva.")

    def withdraw(self, amount):
        #Retrage bani din cont
        if amount <= 0:
            print("Eroare! Suma trebuie sa fie pozitiva.")
        elif amount > self._balance:
            print("Eroare! Sold insuficient. Sold actual:", self._balance)
        else:
            self._balance = self._balance - amount
            print("Retragere reusita! Sold nou:", self._balance)

    def get_balance(self):
        #Returneaza soldul curent
        return self._balance

#Program principal
try:
    print("=== Sistem Bancar ===")

    initial_input = input("Introdu soldul initial al contului: ")

    if initial_input == "":
        print("Eroare! Nu ai introdus nimic.")
    else:
        initial_balance = float(initial_input)

        if initial_balance < 0:
            print("Eroare! Soldul initial nu poate fi negativ.")
        else:
            #Instantiaza obiectul BankAccount
            account = BankAccount(initial_balance)
            print("Cont creat cu succes! Sold:", account.get_balance())

            #Meniu interactiv
            while True:
                print("\n1. Depune bani")
                print("2. Retrage bani")
                print("3. Vezi sold")
                print("4. Iesire")

                choice = input("Alege o optiune: ")

                if choice == "1":
                    amount_input = input("Introdu suma de depus: ")
                    if amount_input == "":
                        print("Eroare! Nu ai introdus suma.")
                    else:
                        amount = float(amount_input)
                        account.deposit(amount)

                elif choice == "2":
                    amount_input = input("Introdu suma de retras: ")
                    if amount_input == "":
                        print("Eroare! Nu ai introdus suma.")
                    else:
                        amount = float(amount_input)
                        account.withdraw(amount)

                elif choice == "3":
                    print("Sold curent:", account.get_balance())

                elif choice == "4":
                    print("La revedere!")
                    break

                else:
                    print("Optiune invalida!")

except ValueError:
    print("Eroare! Te rog introdu valori numerice valide.")
except Exception as e:
    print("Eroare! A aparut o problema:", e)
