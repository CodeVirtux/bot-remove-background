# Classe de base Employe
class Employe:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def calculer_salaire_mensuel(self):
        pass  # Methode a redefinir dans les classes enfants

    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


# Employe Permanent
class EmployePermanent(Employe):
    def __init__(self, nom, age, salaire_fixe):
        super().__init__(nom, age)
        self.salaire_fixe = salaire_fixe

    def calculer_salaire_mensuel(self):
        return self.salaire_fixe

    def afficher_details(self):
        super().afficher_details()
        print(f"Type: Employe Permanent, Salaire: {self.calculer_salaire_mensuel()} DA")


# Ouvrier Saisonnier
class OuvrierSaisonnier(Employe):
    def __init__(self, nom, age, salaire_horaire, heures_travaillees):
        super().__init__(nom, age)
        self.salaire_horaire = salaire_horaire
        self.heures_travaillees = heures_travaillees

    def calculer_salaire_mensuel(self):
        return self.salaire_horaire * self.heures_travaillees

    def afficher_details(self):
        super().afficher_details()
        print(f"Type: Ouvrier Saisonnier, Heures: {self.heures_travaillees}, Salaire: {self.calculer_salaire_mensuel()} DA")


# Superviseur Recolte
class SuperviseurRecolte(Employe):
    def __init__(self, nom, age, salaire_fixe, bonus):
        super().__init__(nom, age)
        self.salaire_fixe = salaire_fixe
        self.bonus = bonus

    def calculer_salaire_mensuel(self):
        return self.salaire_fixe + self.bonus

    def afficher_details(self):
        super().afficher_details()
        print(f"Type: Superviseur Recolte, Salaire fixe: {self.salaire_fixe}, Bonus: {self.bonus}, Salaire total: {self.calculer_salaire_mensuel()} DA")


# Test du systeme
employes = [
    EmployePermanent("Ahmed", 45, 60000),
    OuvrierSaisonnier("Fatima", 32, 500, 120),
    SuperviseurRecolte("Youssef", 40, 70000, 15000),
    OuvrierSaisonnier("Ali", 28, 450, 100)
]

for emp in employes:
    emp.afficher_details()
    print("--------------------------")
