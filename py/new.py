def ajouter(stock):
    nom= input('ajouter nom le prodiut: ')
    quantite= int(input('ajouter la quantite: '))
    prix=float(input('ajouter le prix: '))
    

    stock.append({"nom": nom, "quantite": quantite, "prix": prix})
    print(f"Le produit '{nom}' a été ajouté avec succès.")

def supprimer_produit(stock):
    nom= input("Entrez le nom du produit à supprimer : ")

def mettre_a_jour_quantite(stock):
    nom = input("Entrez le nom du produit à mettre à jour : ")

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
