from abc import ABC, abstractmethod

class MoyenPaiement(ABC):
    @abstractmethod
    def payer(self, montant):
        pass



class CarteBancaire(MoyenPaiement):
    def __init__(self, numero_carte):
        self.numero_carte = numero_carte
    
    def payer(self, montant):
        print(f"Paiement de {montant}€ effectué par carte bancaire (numéro: {self.numero_carte[-4:]})")

class PayPal(MoyenPaiement):
    def __init__(self, email):
        self.email = email
    
    def payer(self, montant):
        print(f"Paiement de {montant}€ effectué via PayPal (email: {self.email})")

class Crypto(MoyenPaiement):
    def __init__(self, adresse_portefeuille):
        self.adresse_portefeuille = adresse_portefeuille
    
    def payer(self, montant):
        print(f"Paiement de {montant}€ effectué en crypto-monnaie (adresse: {self.adresse_portefeuille[:8]}...)")


if __name__ == "__main__":

    carte = CarteBancaire("1234567812345678")
    paypal = PayPal("client@example.com")
    crypto = Crypto("1A2b3C4d5E6f7G8h9I0j")
    

    moyens_paiement = [carte, paypal, crypto]
    

    montants = [50.99, 120.50, 75.25]
    
    for i, moyen in enumerate(moyens_paiement):
        moyen.payer(montants[i])