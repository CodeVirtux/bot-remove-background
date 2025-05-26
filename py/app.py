# num1=input("enter the ferst nomber: ")
# num2=input("enter the second nomber: ")
# adition= int(num1)+int(num2)
# print(adition)
# ============================================
# color= input("enter a color: ")
# noun= input("enter a noun: ")
# adjective= input("enter an adjective: ")
# print("car is "+color)
# print(noun+" is big dog hhh")
# print("hi 🖐️ you adjective is "+adjective)
# ===========================================
# brother= ["ahmad","hh","loka","sara","bomba"]
# brother[0]= "sar"
# print(brother[1])
# ============================================
# fast=["rout","font","codnet"]
# best=["speed","fista","abraham"]
# fast.append("roooooooono")
# print(fast)
# ==========================================
# second= int(input("enter nomber second please: "))
# hours= second//3600
# minuts= (second%3600)//60
# second= second%60
# print(f"the deraction is: {hours} hours; and {minuts} munits and {second} second.")
# ================================================
# use= "ISTA"
# pw= "ista@2024"
# n=input("entrer le nom: ")
# p=input("entrer le mot de passe: ")
# if n==use and p==pw :
#   print("binvenue")
# else:
#   print("le nom ou le mot de passe est incorrectes")
# ====================================================
# tut="top","git",55,44
# print(tut.index(44))
#print(tire.index("fifa"))



import random

# Générer un nombre aléatoire entre 1 et 100
nombre_a_deviner = random.randint(1, 100)

# Initialiser le compteur de tentatives
compteur_tentatives = 0

print("Bienvenue dans le jeu 'Deviner un nombre' !")
print("Le programme a choisi un nombre entre 1 et 100.")
print("Essayez de le deviner !")

# Boucle pour deviner le nombre
while True:
    # Demander une entrée à l'utilisateur
    tentative = int(input("Entrez votre nombre : "))
    compteur_tentatives += 1  # Incrémenter le compteur

    # Comparer la tentative avec le nombre à deviner
    if tentative < nombre_a_deviner:
        print("Le nombre est plus grand !")
    elif tentative > nombre_a_deviner:
        print("Le nombre est plus petit !")
    else:
        # Si l'utilisateur trouve le bon nombre
        print(f"Félicitations ! Vous avez trouvé le nombre après {compteur_tentatives} tentatives.")
        break  # Sortir de la boucle

