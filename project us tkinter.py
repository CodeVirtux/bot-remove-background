import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Liste pour stocker les livres
bibliotheque = []

def ajouter_livre():
    titre = entree_titre.get()
    auteur = entree_auteur.get()
    annee = entree_annee.get()

    if titre and auteur and annee:
        bibliotheque.append({'titre': titre, 'auteur': auteur, 'annee': annee})
        rafraichir_liste()
        entree_titre.delete(0, tk.END)
        entree_auteur.delete(0, tk.END)
        entree_annee.delete(0, tk.END)
    else:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")

def supprimer_livre():
    selection = liste_livres.selection()
    if selection:
        index = int(selection[0])
        del bibliotheque[index]
        rafraichir_liste()
    else:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner un livre à supprimer.")

def rechercher_livre():
    terme_recherche = entree_recherche.get().lower()
    if not terme_recherche:
        rafraichir_liste()
        return
    
    resultats = []
    for livre in bibliotheque:
        if (terme_recherche in livre['titre'].lower() or 
            terme_recherche in livre['auteur'].lower() or 
            terme_recherche in livre['annee'].lower()):
            resultats.append(livre)
    
    for i in liste_livres.get_children():
        liste_livres.delete(i)
    for i, livre in enumerate(resultats):
        liste_livres.insert('', 'end', iid=i, values=(livre['titre'], livre['auteur'], livre['annee']))

def afficher_tous():
    entree_recherche.delete(0, tk.END)
    rafraichir_liste()

def rafraichir_liste():
    for i in liste_livres.get_children():
        liste_livres.delete(i)
    for i, livre in enumerate(bibliotheque):
        liste_livres.insert('', 'end', iid=i, values=(livre['titre'], livre['auteur'], livre['annee']))

# Interface utilisateur
fenetre = tk.Tk()
fenetre.title("Gestion de Bibliothèque")

# Frame pour les logos
frame_logos = tk.Frame(fenetre)
frame_logos.grid(row=0, column=0, columnspan=4, pady=10, sticky='ew')

# Logo ISTA (left) - using placeholder
try:
    img_ista = Image.open("ista_logo.png")  # Replace with actual path
    img_ista = img_ista.resize((100, 50), Image.LANCZOS)
    logo_ista = ImageTk.PhotoImage(img_ista)
    label_ista = tk.Label(frame_logos, image=logo_ista)
    label_ista.image = logo_ista
    label_ista.pack(side='left', padx=10)
except:
    label_ista = tk.Label(frame_logos, text="ISTA ", bg='lightgray', width=15, height=3)
    label_ista.pack(side='left', padx=10)

# Title
label_titre = tk.Label(frame_logos, text="Gestion de Bibliothèque", font=('Arial', 16, 'bold'))
label_titre.pack(side='left', expand=True)

# Logo Bibliothèque (right) - using placeholder
try:
    img_biblio = Image.open("library.png")  # Replace with actual path
    img_biblio = img_biblio.resize((100, 50), Image.LANCZOS)
    logo_biblio = ImageTk.PhotoImage(img_biblio)
    label_biblio = tk.Label(frame_logos, image=logo_biblio)
    label_biblio.image = logo_biblio
    label_biblio.pack(side='right', padx=10)
except:
    label_biblio = tk.Label(frame_logos, text="Library ", bg='lightgray', width=15, height=3)
    label_biblio.pack(side='right', padx=10)

# Frame pour les entrées
frame_entrees = tk.Frame(fenetre)
frame_entrees.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Label(frame_entrees, text="Titre:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entree_titre = tk.Entry(frame_entrees, width=30)
entree_titre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrees, text="Auteur:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entree_auteur = tk.Entry(frame_entrees, width=30)
entree_auteur.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrees, text="Année:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entree_annee = tk.Entry(frame_entrees, width=30)
entree_annee.grid(row=2, column=1, padx=5, pady=5)

# Frame pour les boutons d'action
frame_boutons = tk.Frame(fenetre)
frame_boutons.grid(row=2, column=0, columnspan=2, pady=5)

tk.Button(frame_boutons, text="Ajouter Livre", command=ajouter_livre).grid(row=0, column=0, padx=5)
tk.Button(frame_boutons, text="Supprimer Livre", command=supprimer_livre).grid(row=0, column=1, padx=5)

# Frame pour la recherche
frame_recherche = tk.Frame(fenetre)
frame_recherche.grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(frame_recherche, text="Rechercher:").grid(row=0, column=0, padx=5)
entree_recherche = tk.Entry(frame_recherche, width=30)
entree_recherche.grid(row=0, column=1, padx=5)
tk.Button(frame_recherche, text="Rechercher", command=rechercher_livre).grid(row=0, column=2, padx=5)
tk.Button(frame_recherche, text="Afficher Tous", command=afficher_tous).grid(row=0, column=3, padx=5)

# Liste des livres
colonnes = ("Titre", "Auteur", "Année")
liste_livres = ttk.Treeview(fenetre, columns=colonnes, show='headings', height=10)
for col in colonnes:
    liste_livres.heading(col, text=col)
    liste_livres.column(col, width=150)
liste_livres.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ajouter une barre de défilement
scrollbar = ttk.Scrollbar(fenetre, orient="vertical", command=liste_livres.yview)
scrollbar.grid(row=4, column=2, sticky='ns')
liste_livres.configure(yscrollcommand=scrollbar.set)

fenetre.mainloop()