import tkinter as tk
from tkinter import ttk  # Importer le module ttk pour utiliser la barre de progression
from PIL import Image, ImageTk

class CombatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Combat Pokémon")

        # Définir une taille initiale plus grande (par exemple, 800x400)
        self.master.geometry("800x400")

        # Données des Pokémon
        self.pokemon1_name = "Pikachu"
        self.pokemon1_image_path = "pikachu.png"  # Remplacez par le chemin de votre image
        self.pokemon2_name = "bulbisar"
        self.pokemon2_image_path = "bulbisar.png"  # Remplacez par le chemin de votre image

        # Taille maximale des images
        self.max_image_width = 150
        self.max_image_height = 150

        # Créer des cadres pour les Pokémon
        self.pokemon1_frame = tk.Frame(master)
        self.pokemon1_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.pokemon2_frame = tk.Frame(master)
        self.pokemon2_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Affichage du Pokémon 1 dans le cadre à gauche
        self.pokemon1_label = tk.Label(self.pokemon1_frame, text=self.pokemon1_name)
        self.pokemon1_label.grid(row=0, column=0, pady=5)

        self.pokemon1_health = ttk.Progressbar(self.pokemon1_frame, orient=tk.HORIZONTAL, length=self.max_image_width)
        self.pokemon1_health.grid(row=1, column=0, pady=5)

        self.pokemon1_image = self.load_and_resize_image(self.pokemon1_image_path)
        self.pokemon1_image_label = tk.Label(self.pokemon1_frame, image=self.pokemon1_image)
        self.pokemon1_image_label.grid(row=2, column=0, pady=5)

        # Affichage du Pokémon 2 dans le cadre à droite
        self.pokemon2_label = tk.Label(self.pokemon2_frame, text=self.pokemon2_name)
        self.pokemon2_label.grid(row=0, column=0, pady=5)

        self.pokemon2_health = ttk.Progressbar(self.pokemon2_frame, orient=tk.HORIZONTAL, length=self.max_image_width)
        self.pokemon2_health.grid(row=1, column=0, pady=5)

        self.pokemon2_image = self.load_and_resize_image(self.pokemon2_image_path)
        self.pokemon2_image_label = tk.Label(self.pokemon2_frame, image=self.pokemon2_image)
        self.pokemon2_image_label.grid(row=2, column=0, pady=5)

        # Initialiser la barre de vie à 100%
        self.set_health(self.pokemon1_health, 100)
        self.set_health(self.pokemon2_health, 100)

    def load_and_resize_image(self, image_path):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((self.max_image_width, self.max_image_height))
        return ImageTk.PhotoImage(resized_image)

    def set_health(self, health_bar, value):
        health_bar["value"] = value

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CombatApp(root)
    app.run()
