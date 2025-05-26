#Abdellah Ait-si

def afficher_menu():
    print("\n--- Menu de Gestion de Stock ---")
    print("1. Ajouter un produit")
    print("2. Supprimer un produit")
    print("3. Mettre à jour la quantité d'un produit")
    print("4. Afficher la liste des produits")
    print("5. Calculer la valeur totale du stock")
    print("6. Quitter")


def ajouter_produit(stock):
    nom = input("Entrez le nom du produit : ").strip().capitalize()
    quantite = int(input("Entrez la quantité disponible : "))
    prix = float(input("Entrez le prix unitaire : "))
    

    for produit in stock:
        if produit["nom"] == nom:
            print("Ce produit existe déjà. Utilisez l'option de mise à jour.")
            return

    stock.append({"nom": nom, "quantite": quantite, "prix": prix})
    print(f"Le produit '{nom}' a été ajouté avec succès.")


def supprimer_produit(stock):
    nom = input("Entrez le nom du produit à supprimer : ")
    

    for produit in stock:
        if produit["nom"] == nom:
            stock.remove(produit)
            print(f"Le produit '{nom}' a été supprimé.")
            return
    
    print(f"Le produit '{nom}' n'existe pas dans le stock.")


def mettre_a_jour_quantite(stock):
    nom = input("Entrez le nom du produit à mettre à jour : ").strip().capitalize()
    

    for produit in stock:
        if produit["nom"] == nom:
            nouvelle_quantite = int(input("Entrez la nouvelle quantité : "))
            produit["quantite"] = nouvelle_quantite
            print(f"La quantité du produit '{nom}' a été mise à jour.")
            return
    
    print(f"Le produit '{nom}' n'existe pas dans le stock.")


def afficher_stock(stock):
    if not stock:
        print("Le stock est vide.")
    else:
        print("\n--- Liste des Produits ---")
        for produit in stock:
            print(f"Nom: {produit['nom']}, Quantité: {produit['quantite']}, Prix unitaire: {produit['prix']} €")


def calculer_valeur_totale(stock):
    valeur_totale = sum(produit["quantite"] * produit["prix"] for produit in stock)
    print(f"La valeur totale du stock est de {valeur_totale} €.")


def trier_produits(stock):
    print("\n--- Trier les Produits ---")
    print("1. Trier par nom")
    print("2. Trier par quantité")
    print("3. Trier par prix")
    choix_tri = input("Choisissez une option de tri (1-3) : ")
    
    if choix_tri == "1":
        stock.sort(key=lambda x: x["nom"])
        print("Produits triés par nom.")
    elif choix_tri == "2":
        stock.sort(key=lambda x: x["quantite"])
        print("Produits triés par quantité.")
    elif choix_tri == "3":
        stock.sort(key=lambda x: x["prix"])
        print("Produits triés par prix.")
    else:
        print("Option de tri invalide.")


def main():
    stock = [] 
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6) : ").strip()
        
        if choix == "1":
            ajouter_produit(stock)
        elif choix == "2":
            supprimer_produit(stock)
        elif choix == "3":
            mettre_a_jour_quantite(stock)
        elif choix == "4":
            afficher_stock(stock)
        elif choix == "5":
            calculer_valeur_totale(stock)
        elif choix == "6":
            print("Merci d'avoir utilisé le gestionnaire de stock. Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 6.")


if __name__ == "__main__":
    main()