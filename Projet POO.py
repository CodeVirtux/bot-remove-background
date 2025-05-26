from datetime import datetime, timedelta

# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee_publication, isbn):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.isbn = isbn
        self.disponible = True

    def afficher_details(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"Titre : {self.titre}\nAuteur : {self.auteur}\nAnnée : {self.annee_publication}\nISBN : {self.isbn}\nStatut : {statut}")

    def emprunter(self):
        self.disponible = False

    def retourner(self):
        self.disponible = True

# Classe Emprunt
class Emprunt:
    def __init__(self, livre, membre, date_emprunt, date_retour_prevue):
        self.livre = livre
        self.membre = membre
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue

    def afficher_details(self):
        print(f"Livre : {self.livre.titre}\nMembre : {self.membre.nom}\nDate emprunt : {self.date_emprunt.strftime('%d-%m-%Y')}\nRetour prévu : {self.date_retour_prevue.strftime('%d-%m-%Y')}")

    def prolonger_emprunt(self, jours):
        self.date_retour_prevue += timedelta(days=jours)

# Classe Membre
class Membre:
    def __init__(self, nom, numero_membre):
        self.nom = nom
        self.numero_membre = numero_membre
        self.livres_empruntes = []

    def emprunter_livre(self, livre, date_emprunt, date_retour):
        if livre.disponible:
            emprunt = Emprunt(livre, self, date_emprunt, date_retour)
            self.livres_empruntes.append(emprunt)
            livre.emprunter()
            print(f"{self.nom} a emprunté le livre : {livre.titre}")
        else:
            print(f"Le livre '{livre.titre}' n'est pas disponible.")

    def retourner_livre(self, emprunt):
        if emprunt in self.livres_empruntes:
            emprunt.livre.retourner()
            self.livres_empruntes.remove(emprunt)
            print(f"{self.nom} a retourné le livre : {emprunt.livre.titre}")
        else:
            print("Emprunt non trouvé.")

    def afficher_livres_empruntes(self):
        if not self.livres_empruntes:
            print(f"{self.nom} n'a emprunté aucun livre.")
        else:
            for emprunt in self.livres_empruntes:
                emprunt.afficher_details()

# Classe Bibliothèque
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []
        self.membres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def supprimer_membre(self, numero):
        self.membres = [m for m in self.membres if m.numero_membre != numero]

    def afficher_livres_disponibles(self):
        disponibles = [livre for livre in self.livres if livre.disponible]
        if not disponibles:
            print("Aucun livre disponible.")
        for livre in disponibles:
            livre.afficher_details()

    def afficher_membres(self):
        for membre in self.membres:
            print(f"{membre.nom} (ID : {membre.numero_membre})")

    def rechercher_livres_par_auteur(self, auteur):
        livres_trouves = [livre for livre in self.livres if livre.auteur.lower() == auteur.lower()]
        if not livres_trouves:
            print(f"Aucun livre trouvé pour l'auteur : {auteur}")
        for livre in livres_trouves:
            livre.afficher_details()
