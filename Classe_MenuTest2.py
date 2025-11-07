import tkinter as tk
from tkinter import messagebox

# --- Fonction de gestion des actions ---
def action_menu(option):
    """
    Fonction appelée lorsqu'on clique sur un bouton du menu.
    """
    if option == "Q":
        reponse = messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?")
        if reponse:
            root.destroy()
    else:
        messagebox.showinfo("Information", f"Vous avez choisi : {option}")

# --- Création de la fenêtre principale ---
root = tk.Tk()
root.title("📚 Bibliothèque municipale")
root.geometry("1000x800")
root.config(bg="#1e1e2f")  # Couleur de fond principale (bleu nuit)

# --- Titre principal ---
label_titre = tk.Label(
    root,
    text="Bienvenue à votre bibliothèque\n« Médiathèque de Paris »",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f",
    fg="#f1c40f",
    pady=20
)
label_titre.pack()

# --- Cadre pour les boutons ---
frame_menu = tk.Frame(root, bg="#2e2e3f", padx=20, pady=20)
frame_menu.pack(pady=10, fill="both", expand=True)

# --- Définition des options du menu ---
options = [
    ("1 - Ajouter adhérent", "Ajouter adhérent", "#27ae60"),
    ("2 - Supprimer adhérent", "Supprimer adhérent", "#c0392b"),
    ("3 - Afficher tous les adhérents", "Afficher tous les adhérents", "#2980b9"),
    ("4 - Ajouter document", "Ajouter document", "#27ae60"),
    ("5 - Supprimer document", "Supprimer document", "#c0392b"),
    ("6 - Afficher tous les documents", "Afficher tous les documents", "#2980b9"),
    ("7 - Ajouter emprunt", "Ajouter emprunt", "#27ae60"),
    ("8 - Retour d’un emprunt", "Retour d’un emprunt", "#f39c12"),
    ("9 - Afficher tous les emprunts", "Afficher tous les emprunts", "#2980b9"),
    ("10 - Prolonger un emprunt", "Prolonger un emprunt", "#f39c12"),
    ("11 - Sauvegarder les modifications", "Sauvegarder les modifications", "#9b59b6"),
    ("Q - Quitter", "Q", "#e74c3c"),
]

# --- Création dynamique des boutons ---
for text, option, color in options:
    bouton = tk.Button(
        frame_menu,
        text=text,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        activebackground="#34495e",
        activeforeground="white",
        relief="raised",
        bd=3,
        padx=10,
        pady=5,
        width=35,
        command=lambda opt=option: action_menu(opt)
    )
    bouton.pack(pady=5)

# --- Pied de page ---
footer = tk.Label(
    root,
    text="© 2024 - Gestion de bibliothèque",
    bg="#1e1e2f",
    fg="gray",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=10)

# --- Lancement du programme ---
root.mainloop()
