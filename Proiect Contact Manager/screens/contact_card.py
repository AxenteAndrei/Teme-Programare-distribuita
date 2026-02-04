# Card Contact - afiseaza un contact in lista

import customtkinter as ctk
from PIL import Image
import os


class ContactCard(ctk.CTkFrame):

    def __init__(self, parent, contact, photo_path: str, on_edit, on_delete, on_favorite):
        super().__init__(parent, height=70, fg_color="#2d2d44", corner_radius=10)
        self.contact, self.on_edit, self.on_delete, self.on_favorite = contact, on_edit, on_delete, on_favorite
        self.buttons_visible = False
        self.pack_propagate(False)
        self._create_widgets(photo_path)

    # Creeaza elementele vizuale ale cardului
    def _create_widgets(self, photo_path: str):
        # Avatar (poza sau prima litera)
        if photo_path and os.path.exists(photo_path):
            try:
                img = ctk.CTkImage(Image.open(photo_path).resize((50, 50)), size=(50, 50))
                self.avatar = ctk.CTkLabel(self, image=img, text="", width=50, height=50, corner_radius=8)
            except:
                self.avatar = self._create_letter_avatar()
        else:
            self.avatar = self._create_letter_avatar()
        self.avatar.pack(side="left", padx=12, pady=10)

        # Nume si telefon
        text_frame = ctk.CTkFrame(self, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True, pady=10)
        self.name_label = ctk.CTkLabel(text_frame, text=self.contact.get_full_name(),
            font=ctk.CTkFont(size=15, weight="bold"), text_color="white", anchor="w")
        self.name_label.pack(anchor="w")
        self.phone_label = ctk.CTkLabel(text_frame, text=self.contact.phone,
            font=ctk.CTkFont(size=12), text_color="#a0a0a0", anchor="w")
        self.phone_label.pack(anchor="w")
        self.text_frame = text_frame

        # Butoanele (ascunse, apar la hover)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        star = ("\u2605", "#f1c40f") if self.contact.favorite else ("\u2606", "#555577")
        buttons = [(star[0], star[1], "#f39c12", self.on_favorite),
                   ("\u270E", "#3498db", "#2980b9", self.on_edit),
                   ("\u2715", "#e74c3c", "#c0392b", self.on_delete)]
        self.btn_widgets = []
        for text, fg_color, hover_color, command in buttons:
            btn = ctk.CTkButton(self.buttons_frame, text=text, width=36, height=36, font=ctk.CTkFont(size=16),
                                fg_color=fg_color, hover_color=hover_color, corner_radius=8, command=command)
            btn.pack(side="left", padx=3)
            self.btn_widgets.append(btn)

        # Leaga evenimentele de hover (mouse pe card)
        for widget in [self, self.avatar, self.text_frame, self.name_label, self.phone_label, self.buttons_frame] + self.btn_widgets:
            widget.bind("<Enter>", self._on_enter)
            widget.bind("<Leave>", self._on_leave)

    # Creeaza avatar cu litera (cand nu e poza)
    def _create_letter_avatar(self):
        return ctk.CTkLabel(self, text=self.contact.get_initials(), width=50, height=50,
            fg_color="#4a4a7e", corner_radius=8, font=ctk.CTkFont(size=20, weight="bold"), text_color="white")

    # Cand mouse-ul intra pe card - arata butoanele
    def _on_enter(self, event):
        self.configure(fg_color="#3d3d5c")
        if not self.buttons_visible:
            self.buttons_frame.pack(side="right", padx=12, pady=10)
            self.buttons_visible = True

    # Cand mouse-ul iese de pe card - ascunde butoanele
    def _on_leave(self, event):
        widget = self.winfo_containing(*self.winfo_pointerxy())
        all_widgets = [self, self.avatar, self.text_frame, self.name_label, self.phone_label, self.buttons_frame] + self.btn_widgets
        if widget not in all_widgets:
            self.configure(fg_color="#2d2d44")
            self.buttons_frame.pack_forget()
            self.buttons_visible = False
