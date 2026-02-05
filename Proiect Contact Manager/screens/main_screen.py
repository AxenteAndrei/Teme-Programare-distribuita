# Ecran Principal - lista de contacte cu sectiuni alfabetice

import customtkinter as ctk
from tkinter import messagebox
from screens.contact_card import ContactCard


class MainScreen(ctk.CTkFrame):

    def __init__(self, parent, manager, on_add, on_edit):
        super().__init__(parent, fg_color="transparent")
        self.manager, self.on_add, self.on_edit = manager, on_add, on_edit
        self._create_ui()

    # Creeaza interfata ecranului principal
    def _create_ui(self):
        # Header 
        header = ctk.CTkFrame(self, height=60, fg_color="#1a1a2e")
        header.pack(fill="x")
        header.pack_propagate(False)
        ctk.CTkLabel(header, text="Contact Manager", font=ctk.CTkFont(size=24, weight="bold"),
                     text_color="white").pack(side="left", padx=20, pady=15)

        # Buton de adaugare contact
        ctk.CTkButton(header, text="+", width=40, height=40, font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="#4CAF50", hover_color="#45a049", corner_radius=20, command=self.on_add
        ).pack(side="right", padx=20, pady=10)

        # Lista de contacte 
        self.list_frame = ctk.CTkScrollableFrame(self, fg_color="transparent",
            scrollbar_button_color="#3a3a5e", scrollbar_button_hover_color="#4a4a7e")
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Reincarca lista de contacte
    def refresh(self):
        # Sterge widget-urile vechi
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Mesaj daca nu sunt contacte
        if not self.manager.contacts:
            ctk.CTkLabel(self.list_frame, text="No contacts yet.\nPress + to add one.",
                font=ctk.CTkFont(size=16), text_color="gray").pack(pady=50)
            return

        # Creeaza lista cu indexuri si sorteaza alfabetic dupa nume
        contacts = sorted(enumerate(self.manager.contacts), key=lambda x: x[1].get_full_name().lower())
        favorites = [(index, contact) for index, contact in contacts if contact.favorite]
        regular = [(index, contact) for index, contact in contacts if not contact.favorite]

        # Afiseaza sectiunea Favorites (daca exista)
        if favorites:
            self._add_section_header("\u2605 Favorites")
            for index, contact in favorites:
                self._add_contact_card(index, contact)

        # Grupeaza contactele dupa prima litera
        current_letter = ""
        for index, contact in regular:
            letter = contact.get_full_name()[0].upper()
            if letter != current_letter:
                current_letter = letter
                self._add_section_header(letter)
            self._add_contact_card(index, contact)

    # Adauga un header de sectiune (A, B, C, etc)
    def _add_section_header(self, letter: str):
        ctk.CTkLabel(self.list_frame, text=letter, font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#888888", anchor="w").pack(fill="x", padx=10, pady=(15, 5))

    # Adauga un card de contact in lista
    def _add_contact_card(self, index: int, contact):
        ContactCard(self.list_frame, contact, self.manager.get_photo_path(contact.photo),
            lambda i=index: self.on_edit(i), lambda i=index: self._delete(i),
            lambda i=index: self._toggle_favorite(i)).pack(fill="x", pady=3, padx=5)

    # Sterge un contact (cu confirmare)
    def _delete(self, index: int):
        contact = self.manager.get_contact(index)
        if messagebox.askyesno("Confirm", f"Delete {contact.get_full_name()}?"):
            self.manager.delete_contact(index)
            self.refresh()

    # Schimba statusul de favorit
    def _toggle_favorite(self, index: int):
        self.manager.toggle_favorite(index)
        self.refresh()
