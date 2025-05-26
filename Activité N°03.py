class Livre:
    def __init__(self, titre, auteur, annee_publication, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.disponible = disponible
    
    def afficher_info(self):
        dispo_text = "Disponible" if self.disponible else "Emprunté"
        print(f"Titre : {self.titre}\nAuteur : {self.auteur}\nAnnée de publication : {self.annee_publication}\nStatut : {dispo_text}\n")
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Vous avez emprunté le livre '{self.titre}'.")
        else:
            print(f"Désolé, le livre '{self.titre}' est déjà emprunté.")
    
    def rendre(self):
        self.disponible = True
        print(f"Vous avez rendu le livre '{self.titre}'.")

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre2 = Livre("1984", "George Orwell", 1949)
livre3 = Livre("L'Étranger", "Albert Camus", 1942)

livre1.afficher_info()
livre2.afficher_info()
livre3.afficher_info()

livre1.emprunter()
livre1.afficher_info()

livre1.emprunter()

livre1.rendre()
livre1.afficher_info()
