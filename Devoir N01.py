class Personne:
    def __init__(self, cin, nom):
        self.__cin = cin  
        self.__nom = nom  

    def modifier_info(self, cin, nom):
        self.__cin = cin
        self.__nom = nom

    def afficher(self):
        print(f"CIN: {self.__cin}, Nom: {self.__nom}")


p1 = Personne("AB123456", "ahmad Dupont")

try:
    print(p1.__cin)
except AttributeError:
    print("Impossible d'accéder directement à __cin car c'est un attribut privé.")

try:
    print(p1.__nom)
except AttributeError:
    print("Impossible d'accéder directement à __nom car c'est un attribut privé.")


p1.afficher()
p1.modifier_info("CD789012", "hamza Martin")
p1.afficher()
