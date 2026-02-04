# Clasa Contact - reprezinta un singur contact

class Contact:

    def __init__(self, name: str, phone: str, email: str = "", photo: str = "", surname: str = "", favorite: bool = False):
        self.name, self.surname, self.phone = name, surname, phone
        self.email, self.photo, self.favorite = email, photo, favorite

    # Transforma contactul in dictionar pentru salvare in JSON
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "email": self.email,
            "photo": self.photo,
            "favorite": self.favorite
        }

    # Creeaza un Contact din dictionar (citit din JSON)
    @staticmethod
    def from_dict(data: dict):
        return Contact(data.get("name", ""), data.get("phone", ""), data.get("email", ""),
                       data.get("photo", ""), data.get("surname", ""), data.get("favorite", False))

    # Returneaza prima litera din nume (pentru avatar)
    def get_initials(self) -> str:
        return self.name[0].upper() if self.name else "?"

    # Returneaza numele complet (nume + prenume)
    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}" if self.surname else self.name
