# Ecran Formular - adauga sau editeaza un contact

import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
import os, re


class FormScreen(ctk.CTkFrame):

    def __init__(self, parent, manager, on_back):
        super().__init__(parent, fg_color="transparent")
        self.manager, self.on_back = manager, on_back
        self.edit_index, self.current_photo, self._temp_photo_path = None, "", None
        self._create_ui()

    # Creeaza interfata formularului
    def _create_ui(self):
        # Header
        header = ctk.CTkFrame(self, height=60, fg_color="#1a1a2e")
        header.pack(fill="x")
        header.pack_propagate(False)
        ctk.CTkButton(header, text="\u2190", width=40, height=40, font=ctk.CTkFont(size=20, weight="bold"),
            fg_color="transparent", hover_color="#3a3a5e", command=self.on_back).pack(side="left", padx=10, pady=10)
        self.title_label = ctk.CTkLabel(header, text="Add Contact",
            font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
        self.title_label.pack(side="left", padx=10, pady=15)

        # Formular (scrollabil)
        form = ctk.CTkScrollableFrame(self, fg_color="transparent")
        form.pack(fill="both", expand=True, padx=25, pady=15)

        # Avatar (poza sau litera)
        self.avatar_label = ctk.CTkLabel(form, text="?", width=90, height=90, fg_color="#4a4a7e",
            corner_radius=10, font=ctk.CTkFont(size=36, weight="bold"), text_color="white")
        self.avatar_label.pack(pady=10)

        # Butoane pentru poza
        btn_frame = ctk.CTkFrame(form, fg_color="transparent")
        btn_frame.pack(pady=8)
        ctk.CTkButton(btn_frame, text="Choose Photo", width=110, height=28, font=ctk.CTkFont(size=12),
            fg_color="#555577", hover_color="#666688", corner_radius=6, command=self._choose_photo).pack(side="left", padx=4)
        ctk.CTkButton(btn_frame, text="Remove", width=70, height=28, font=ctk.CTkFont(size=12),
            fg_color="#777777", hover_color="#888888", corner_radius=6, command=self._remove_photo).pack(side="left", padx=4)

        # Campurile formularului
        self.name_entry = self._create_field(form, "Name *", "")
        self.name_entry.bind("<KeyRelease>", self._update_avatar)
        self.surname_entry = self._create_field(form, "Surname (optional)", "")
        self.phone_entry = self._create_field(form, "Phone *", "")
        self.phone_entry.bind("<KeyRelease>", self._filter_phone)
        self.email_entry = self._create_field(form, "Email", "")

        # Buton salvare
        self.save_btn = ctk.CTkButton(form, text="Save Contact", height=45, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#4CAF50", hover_color="#45a049", corner_radius=8, command=self._save)
        self.save_btn.pack(fill="x", pady=(25, 8))

        # Buton stergere (doar la editare)
        self.delete_btn = ctk.CTkButton(form, text="Delete Contact", height=45, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#e74c3c", hover_color="#c0392b", corner_radius=8, command=self._delete)

    # Creeaza un camp cu label si input
    def _create_field(self, parent, label: str, placeholder: str) -> ctk.CTkEntry:
        ctk.CTkLabel(parent, text=label, font=ctk.CTkFont(size=13), text_color="#a0a0a0").pack(anchor="w", pady=(12, 4))
        entry = ctk.CTkEntry(parent, height=42, font=ctk.CTkFont(size=15), placeholder_text=placeholder,
            corner_radius=8, border_width=1, border_color="#3a3a5e")
        entry.pack(fill="x")
        return entry

    # Filtreaza telefonul - doar cifre, +, - si spatii
    def _filter_phone(self, event=None):
        current = self.phone_entry.get()
        filtered = re.sub(r'[^0-9+\-\s]', '', current)
        if current != filtered:
            pos = self.phone_entry.index("insert")
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, filtered)
            self.phone_entry.icursor(min(pos, len(filtered)))

    # Deschide dialogul pentru alegere poza
    def _choose_photo(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All", "*.*")])
        if path:
            self._show_photo(path, is_new=True)

    # Afiseaza poza in avatar
    def _show_photo(self, path: str, is_new: bool = False):
        try:
            img = ctk.CTkImage(Image.open(path).resize((90, 90)), size=(90, 90))
            self.avatar_label.configure(image=img, text="")
            self.avatar_label.image = img
            self._temp_photo_path = path if is_new else None
            self.current_photo = "pending" if is_new else os.path.basename(path)
        except Exception as error:
            messagebox.showerror("Error", f"Could not load image: {error}")

    # Sterge poza selectata
    def _remove_photo(self):
        self._temp_photo_path, self.current_photo = None, ""
        self._update_avatar()

    # Actualizeaza avatarul cu prima litera din nume
    def _update_avatar(self, event=None):
        if self.current_photo:
            return
        letter = self.name_entry.get()[0].upper() if self.name_entry.get() else "?"
        self.avatar_label.configure(image=None, text=letter, fg_color="#4a4a7e")

    # Pregateste formularul pentru adaugare contact nou
    def setup_add(self):
        self.edit_index, self.current_photo, self._temp_photo_path = None, "", None
        self.title_label.configure(text="Add Contact")
        self.delete_btn.pack_forget()
        self._clear()

    # Pregateste formularul pentru editare contact existent
    def setup_edit(self, index: int):
        self.edit_index, self._temp_photo_path = index, None
        contact = self.manager.get_contact(index)
        if not contact:
            return
        self.title_label.configure(text="Edit Contact")
        self.delete_btn.pack(fill="x", pady=8)
        self._clear()
        self.name_entry.insert(0, contact.name)
        self.surname_entry.insert(0, contact.surname)
        self.phone_entry.insert(0, contact.phone)
        self.email_entry.insert(0, contact.email)
        self.current_photo = contact.photo
        if contact.photo:
            path = self.manager.get_photo_path(contact.photo)
            if path:
                self._show_photo(path, is_new=False)
        else:
            self._update_avatar()

    # Goleste toate campurile
    def _clear(self):
        for entry in [self.name_entry, self.surname_entry, self.phone_entry, self.email_entry]:
            entry.delete(0, "end")
        self.current_photo = ""
        self.avatar_label.configure(image=None, text="?", fg_color="#4a4a7e")

    # Salveaza contactul (nou sau editat)
    def _save(self):
        name, surname = self.name_entry.get().strip(), self.surname_entry.get().strip()
        phone, email = self.phone_entry.get().strip(), self.email_entry.get().strip()

        # Validari
        if not name:
            return messagebox.showwarning("Validation", "Name is required!")
        if not phone:
            return messagebox.showwarning("Validation", "Phone is required!")
        if len(re.sub(r'[^0-9]', '', phone)) < 6:
            return messagebox.showwarning("Validation", "Phone number too short!")

        # Proceseaza poza
        photo = ""
        if self._temp_photo_path:
            photo = self.manager.import_photo(self._temp_photo_path)
            if self.edit_index is not None:
                old_contact = self.manager.get_contact(self.edit_index)
                if old_contact and old_contact.photo:
                    self.manager.delete_photo(old_contact.photo)
        elif self.current_photo and self.current_photo != "pending":
            photo = self.current_photo

        # Salveaza
        if self.edit_index is None:
            self.manager.add_contact(name, phone, email, photo, surname)
        else:
            favorite = self.manager.get_contact(self.edit_index).favorite
            self.manager.update_contact(self.edit_index, name, phone, email, photo, surname, favorite)
        self.on_back()

    # Sterge contactul curent
    def _delete(self):
        if self.edit_index is not None:
            contact = self.manager.get_contact(self.edit_index)
            if messagebox.askyesno("Confirm", f"Delete {contact.get_full_name()}?"):
                self.manager.delete_contact(self.edit_index)
                self.on_back()
