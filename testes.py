def lire_fichier(nom_fichier):
    """
    Lit un fichier texte contenant des produits et leurs prix.
    Retourne une liste de tuples (produit, prix).
    """
    produits = []
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            # Supprimer les espaces et sauts de ligne, puis séparer produit et prix
            ligne = ligne.strip()
            if ligne:  # Ignorer les lignes vides
                try:
                    produit, prix = ligne.rsplit(maxsplit=1)
                    produits.append((produit, float(prix)))
                except ValueError:
                    print(f"Erreur de format dans la ligne: {ligne}")
    return produits

def calculer_moyenne(produits):
    """
    Calcule la moyenne des prix.
    """
    if not produits:
        return 0
    total = sum(prix for _, prix in produits)
    return total / len(produits)

def trouver_prix_max(produits):
    """
    Retourne le prix le plus élevé.
    """
    if not produits:
        return 0
    return max(prix for _, prix in produits)

def trouver_produit_moins_cher(produits):
    """
    Retourne le nom du produit le moins cher.
    """
    if not produits:
        return "Aucun produit"
    return min(produits, key=lambda x: x[1])[0]

def trier_produits(produits):
    """
    Trie les produits par prix (ordre croissant).
    """
    return sorted(produits, key=lambda x: x[1])

def enregistrer_resultats(nom_fichier, moyenne, prix_max, produit_moins_cher, produits_tries):
    """
    Enregistre les résultats dans un fichier.
    """
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(f"Moyenne des prix: {moyenne:.2f}\n")
        f.write(f"Prix le plus élevé: {prix_max:.2f}\n")
        f.write(f"Produit le moins cher: {produit_moins_cher}\n")
        f.write("\nListe des produits triés par prix (croissant):\n")
        for produit, prix in produits_tries:
            f.write(f"{produit}: {prix:.2f}\n")

def main():
    # Nom du fichier d'entrée et de sortie
    fichier_entree = 'produits.txt'
    fichier_sortie = 'resultats_analyse.txt'
    
    # Lire les produits
    produits = lire_fichier(fichier_entree)
    
    if not produits:
        print("Aucun produit trouvé dans le fichier.")
        return
    
    # Calculer les statistiques
    moyenne = calculer_moyenne(produits)
    prix_max = trouver_prix_max(produits)
    produit_moins_cher = trouver_produit_moins_cher(produits)
    produits_tries = trier_produits(produits)
    
    # Afficher les résultats
    print(f"Moyenne des prix: {moyenne:.2f}")
    print(f"Prix le plus élevé: {prix_max:.2f}")
    print(f"Produit le moins cher: {produit_moins_cher}")
    print("\nListe des produits triés par prix (croissant):")
    for produit, prix in produits_tries:
        print(f"{produit}: {prix:.2f}")
    
    # Enregistrer les résultats
    enregistrer_resultats(fichier_sortie, moyenne, prix_max, produit_moins_cher, produits_tries)
    print(f"\nLes résultats ont été enregistrés dans {fichier_sortie}")

if __name__ == "__main__":
    main()