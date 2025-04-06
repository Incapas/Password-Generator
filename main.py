import sqlite3
import random
from tkinter import messagebox

import pyperclip
import customtkinter as ctk

# Connexion à la base de donnée sqlite
db_connection = sqlite3.connect("database.sqlite")
db_cursor = db_connection.cursor()

def window(container) -> None:

    def get_password_lenght(value) -> None:
        """Met à jour le texte du label affichant la longueur du mot de passe.

        Args:
            value: La nouvelle valeur de la longueur du mot de passe.

        Returns:
            None: Cette fonction ne retourne aucune valeur. Elle modifie l'état du label nommé `label_password_lenght`.
        """
        label_password_lenght.configure(text=f"Longueur du mot de passe : {str(int(value))}")
        return None

    def get_password_options() -> dict:
        """Récupère l'état des options de génération de mot de passe.

            Lit l'état (coché ou non) de différentes cases à cocher de l'interface
            utilisateur correspondant aux types de caractères à inclure dans le
            mot de passe. Active ou désactive également le bouton de génération
            en fonction de la sélection d'au moins une option.

            Returns:
                dict: Un dictionnaire où les clés sont les noms des options de
                    caractères (par exemple, "LatinUpperAlphabet") et les valeurs
                    sont des entiers représentant l'état de la case à cocher.
            """
        check_password_options = {
            "LatinUpperAlphabet": checkbox_latin_uppercase_letters.get(),
            "LatinLowerAlphabet": checkbox_latin_lowercase_letters.get(),
            "ArabicNumerals": checkbox_arabic_numerals.get(),
            "PunctuationCharacters": checkbox_punctuation_characters.get(),
        }
        btn_generate_password.configure(state="normal") if 1 in check_password_options.values() else btn_generate_password.configure(state="disabled")
        return check_password_options

    def generate_password() -> None:
        """Génère un nouveau mot de passe et l'affiche dans le champ de saisie.

        Efface le contenu actuel du champ de saisie du mot de passe, récupère les
        options de caractères sélectionnées, interroge la base de données pour
        obtenir les ensembles de caractères correspondants, génère un mot de passe
        aléatoire en utilisant ces caractères et la longueur spécifiée par le
        slider, insère le nouveau mot de passe dans le champ de saisie et active
        le bouton de copie du mot de passe.

        Returns:
            None: Cette fonction ne retourne aucune valeur.
        """
        entry_password.delete(first_index=0, last_index=len(entry_password.get()))
        password_options = get_password_options()
        password_elements = [element[1] for k, v in password_options.items() if v == 1 for element in db_cursor.execute(f"SELECT * FROM {k}")]
        entry_password.insert(index=0, string="".join(random.choices(password_elements, k=int(slider_password_lenght.get()))))
        btn_copy_password.configure(state="normal")
        return None
    
    def copy_password() -> None:
        """Copie le mot de passe affiché dans le champ de saisie vers le presse-papier.

        Vérifie si le champ de saisie du mot de passe contient un mot de passe.
        Si le champ est vide, affiche un avertissement demandant à l'utilisateur
        de générer un mot de passe. Sinon, copie le contenu du champ de saisie
        dans le presse-papier et affiche un message de confirmation.

        Returns:
            None: Cette fonction ne retourne aucune valeur. Elle interagit avec
                  l'interface utilisateur en affichant des boîtes de message et
                  utilise le presse-papier du système.
        """
        if entry_password.get() == "":
            messagebox.showwarning(message="Veuillez générer un mot de passe !")
        else:
            pyperclip.copy(entry_password.get())
            messagebox.showinfo(message="Le mot de passe a été copié dans le presse papier.")

    # Première section de l'interface graphique
    first_section = ctk.CTkFrame(master=container, fg_color="transparent")
    first_section.pack(fill="x", padx=60, pady=10)

    checkbox_latin_uppercase_letters = ctk.CTkCheckBox(master=first_section, text="Lettres latines majuscules", command=get_password_options)
    checkbox_latin_uppercase_letters.grid(column=0, row=0, padx=10, pady=5)

    checkbox_latin_lowercase_letters = ctk.CTkCheckBox(master=first_section, text="Lettres latines minuscules", command=get_password_options)
    checkbox_latin_lowercase_letters.grid(column=0, row=1, padx=10, pady=5)

    checkbox_arabic_numerals = ctk.CTkCheckBox(master=first_section, text="Chiffres arabes", command=get_password_options)
    checkbox_arabic_numerals.grid(column=1, row=0, padx=10, pady=5, sticky="w")

    checkbox_punctuation_characters = ctk.CTkCheckBox(master=first_section, text="Caractères spéciaux", command=get_password_options)
    checkbox_punctuation_characters.grid(column=1, row=1, padx=10, pady=5, sticky="w")

    # Deuxième section de l'interface graphique
    second_section = ctk.CTkFrame(master=container, fg_color="transparent")
    second_section.pack(fill="x", pady=10)

    label_password_lenght = ctk.CTkLabel(master=second_section, width=300, text="Longueur du mot de passe : 6", anchor="w")
    label_password_lenght.grid(column=0, row=0, padx=(150, 0))

    slider_password_lenght = ctk.CTkSlider(master=second_section, width=400, from_=6, to=60, number_of_steps=54, command=get_password_lenght)
    slider_password_lenght.set(6)
    slider_password_lenght.grid(column=0, row=1, padx=(50, 0))

    # Troisième section de l'interface graphique
    third_section = ctk.CTkFrame(master=app, fg_color="transparent")
    third_section.pack(fill="x", pady=25)

    btn_generate_password = ctk.CTkButton(master=third_section, text="Générer", command=generate_password, state="disabled")
    btn_generate_password.grid(column=0, row=0, padx=(100, 20))

    btn_copy_password = ctk.CTkButton(master=third_section, text="Copier", command=copy_password, state="disabled")
    btn_copy_password.grid(column=1, row=0)

    entry_password = ctk.CTkEntry(master=app)
    entry_password.pack(fill="x", padx=10)

# affichage de la fenêtre
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Générateur de mot de passe")
    app.geometry("500x300+0+0")
    app.resizable(width=False, height=False)
    window(container=app)
    app.mainloop()