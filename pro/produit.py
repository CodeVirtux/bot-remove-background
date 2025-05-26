def lire_fichier(nom_fichier):
    """Lit un fichier et retourne une liste de tuples (produit, prix)."""
    produits = []
    try:
        with open(nom_fichier, "r", encoding="utf-8") as file:
            lignes = file.readlines()
        for ligne in lignes:
            parts = ligne.strip().split()
            if len(parts) == 2:  
                produit, prix = parts[0], parts[1]
                try:
                    prix = float(prix)
                    produits.append((produit, prix))
                except ValueError:
                    continue  
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    return produits

def calculer_moyenne(prix):
    """Retourne la moyenne des prix."""
    return sum(prix) / len(prix) if prix else 0

def trouver_produit_max(produits):
    """Retourne le produit avec le prix le plus élevé."""
    return max(produits, key=lambda x: x[1])

def trouver_produit_min(produits):
    """Retourne le produit avec le prix le plus bas."""
    return min(produits, key=lambda x: x[1])

def trier_produits(produits):
    """Retourne la liste des produits triée par prix croissant."""
    return sorted(produits, key=lambda x: x[1])

def enregistrer_resultats(nom_fichier, moyenne, produit_max, produit_min, produits_tries):
    """Enregistre les résultats dans un fichier."""
    with open(nom_fichier, "w", encoding="utf-8") as file:
        file.write(f"Moyenne des prix: {moyenne:.2f}\n")
        file.write(f"Produit le plus cher: {produit_max[0]} ({produit_max[1]})\n")
        file.write(f"Produit le moins cher: {produit_min[0]} ({produit_min[1]})\n")
        file.write("Produits triés par prix (ordre croissant):\n")
        for produit, prix in produits_tries:
            file.write(f"{produit}: {prix}\n")

nom_fichier = "produit.txt"
produits = lire_fichier(nom_fichier)

if produits:
    liste_prix = [p[1] for p in produits]
    moyenne = calculer_moyenne(liste_prix)
    produit_max = trouver_produit_max(produits)
    produit_min = trouver_produit_min(produits)
    produits_tries = trier_produits(produits)


    print(f"Moyenne des prix: {moyenne:.2f}")
    print(f"Produit le plus cher: {produit_max[0]} ({produit_max[1]})")
    print(f"Produit le moins cher: {produit_min[0]} ({produit_min[1]})")
    print("Produits triés par prix (ordre croissant):")
    for produit, prix in produits_tries:
        print(f"{produit}: {prix}")


    enregistrer_resultats("resultats.txt", moyenne, produit_max, produit_min, produits_tries)
else:
    print("Aucun produit trouvé dans le fichier.")