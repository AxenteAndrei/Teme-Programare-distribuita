# Fisierul principal - porneste aplicatia

import customtkinter as ctk
from manager import ContactManager
from screens import MainScreen, FormScreen


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Contact Manager")
        self.geometry("400x650")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.manager = ContactManager()
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        # Cele 2 ecrane: lista si formular
        self.main_screen = MainScreen(self.container, self.manager, self._open_add, self._open_edit)
        self.form_screen = FormScreen(self.container, self.manager, self._show_main)
        self._show_main()

    # Afiseaza ecranul principal (lista)
    def _show_main(self):
        self.form_screen.pack_forget()
        self.main_screen.pack(fill="both", expand=True)
        self.main_screen.refresh()

    # Deschide formularul pentru contact nou
    def _open_add(self):
        self.form_screen.setup_add()
        self.main_screen.pack_forget()
        self.form_screen.pack(fill="both", expand=True)

    # Deschide formularul pentru editare
    def _open_edit(self, index: int):
        self.form_screen.setup_edit(index)
        self.main_screen.pack_forget()
        self.form_screen.pack(fill="both", expand=True)


# Porneste aplicatia
if __name__ == "__main__":
    App().mainloop()
