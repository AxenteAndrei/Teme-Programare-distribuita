# Manager - se ocupa de lista de contacte si salvarea in fisier

import json, os, shutil, uuid
from models import Contact

# Directorul unde se afla acest fisier (manager.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ContactManager:

    def __init__(self, data_file: str = None, photos_dir: str = None):
        self.data_file = data_file or os.path.join(BASE_DIR, "data", "contacts.json")
        self.photos_dir = photos_dir or os.path.join(BASE_DIR, "photos")
        self.contacts: list = []
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        os.makedirs(self.photos_dir, exist_ok=True)
        self.load_contacts()

    # Incarca contactele din fisierul JSON
    def load_contacts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                self.contacts = [Contact.from_dict(contact) for contact in json.load(file)]

    # Salveaza contactele in fisierul JSON
    def save_contacts(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4, ensure_ascii=False)

    # Adauga un contact nou
    def add_contact(self, name: str, phone: str, email: str = "", photo: str = "", surname: str = "", favorite: bool = False):
        self.contacts.append(Contact(name, phone, email, photo, surname, favorite))
        self.save_contacts()

    # Actualizeaza un contact existent
    def update_contact(self, index: int, name: str, phone: str, email: str = "", photo: str = "", surname: str = "", favorite: bool = False):
        contact = self.contacts[index]
        contact.name, contact.surname, contact.phone = name, surname, phone
        contact.email, contact.photo, contact.favorite = email, photo, favorite
        self.save_contacts()

    # Schimba statusul de favorit (on/off)
    def toggle_favorite(self, index: int):
        self.contacts[index].favorite = not self.contacts[index].favorite
        self.save_contacts()

    # Sterge un contact
    def delete_contact(self, index: int):
        if self.contacts[index].photo:
            self.delete_photo(self.contacts[index].photo)
        del self.contacts[index]
        self.save_contacts()

    # Returneaza un contact dupa index
    def get_contact(self, index: int):
        return self.contacts[index] if 0 <= index < len(self.contacts) else None

    # Copiaza o poza in folderul photos si returneaza numele nou
    def import_photo(self, source: str) -> str:
        if not source or not os.path.exists(source):
            return ""
        new_name = f"{uuid.uuid4().hex[:8]}{os.path.splitext(source)[1]}"
        shutil.copy2(source, os.path.join(self.photos_dir, new_name))
        return new_name

    # Returneaza calea completa catre o poza
    def get_photo_path(self, filename: str) -> str:
        if filename:
            path = os.path.join(self.photos_dir, filename)
            return path if os.path.exists(path) else ""
        return ""

    # Sterge o poza din folder
    def delete_photo(self, filename: str):
        path = os.path.join(self.photos_dir, filename)
        if filename and os.path.exists(path):
            os.remove(path)
