import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connexion à SQLite
conn = sqlite3.connect('Base de données complète projet OM.db')
cursor = conn.cursor()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion de la base de données")

# Ajouter des onglets
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Onglet Joueur
frame_joueur = ttk.Frame(notebook)
notebook.add(frame_joueur, text="Joueur")

tk.Label(frame_joueur, text="Nom").grid(row=0, column=0)
nom_entry = tk.Entry(frame_joueur)
nom_entry.grid(row=0, column=1)

tk.Label(frame_joueur, text="Prénom").grid(row=1, column=0)
prenom_entry = tk.Entry(frame_joueur)
prenom_entry.grid(row=1, column=1)

def ajouter_joueur():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    if nom and prenom:
        try:
            cursor.execute("INSERT INTO JOUEUR (NomJoueur, PrénomJoueur) VALUES (?, ?)", (nom, prenom))
            conn.commit()
            messagebox.showinfo("Succès", "Joueur ajouté avec succès !")
            nom_entry.delete(0, tk.END)
            prenom_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")
    else:
        messagebox.showwarning("Attention", "Veuillez remplir tous les champs !")

tk.Button(frame_joueur, text="Ajouter", command=ajouter_joueur).grid(row=2, column=1)

# Onglet Stade
frame_stade = ttk.Frame(notebook)
notebook.add(frame_stade, text="Stade")

tk.Label(frame_stade, text="Code Stade").grid(row=0, column=0)
code_stade_entry = tk.Entry(frame_stade)
code_stade_entry.grid(row=0, column=1)

tk.Label(frame_stade, text="Nom Stade").grid(row=1, column=0)
nom_stade_entry = tk.Entry(frame_stade)
nom_stade_entry.grid(row=1, column=1)

def ajouter_stade():
    code = code_stade_entry.get()
    nom = nom_stade_entry.get()
    if code and nom:
        try:
            cursor.execute("INSERT INTO STADE (codeStade, NomStade) VALUES (?, ?)", (code, nom))
            conn.commit()
            messagebox.showinfo("Succès", "Stade ajouté avec succès !")
            code_stade_entry.delete(0, tk.END)
            nom_stade_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")
    else:
        messagebox.showwarning("Attention", "Veuillez remplir tous les champs !")

tk.Button(frame_stade, text="Ajouter", command=ajouter_stade).grid(row=2, column=1)

# Lancer l'application
root.mainloop()
conn.close()
