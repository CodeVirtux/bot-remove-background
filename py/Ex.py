dictionnaire: 
# يُستخدم لتخزين مجموعة من القيم المرتبطة بمفاتيح محددة

# Key يجب أن يكون فريدًا اي لا يمكن تكراره ويمكن ان  يكون أرقام أو النصوص

# لنشاء dictionnaire بستخدام {}

#==========================================


#للحصول على قيمة محددة في dictionnaire نستخدم []
print(person["name"])

#لتحديت قيمة Key الموجود في dictionnaire
person["age"] = 35

#لإضافة  Key جدبد  وقيمته
"person["job"] = "Engineer

#لحدف Key وقيمته نستخدم أداة del 
del person["city"]

#لتحقق ما ادا كان المفتاح موجود في dictionnaire نستخدم أداة in
if "name" in person:
    print("The key 'name' exists in the dictionary")

#لعرض جميع  les cler de dictionnaire نستخدم la method ,keys() 
print(list(d.keys()))  

#لعرض جميع les valeur de dictionnaire نستخدم la method values() 
print(list(d.values())) 

#لعرض جميع les cler و les valeur نستخدم la method items() 
print(list(d.items())) 

#لدمج النصوص وقيم المتغيرات في سلسلة واحدة  نستخدم la method f-string 
phrase = f"{d['prenom']} {d['nom']} a {d['age']} ans"

#نستخدم {} باش نبينو فين غادي تدار القيم من dictionnaire




#les xemple:----------------

stok={'name':33}

print(stok['name'])

del stok['name']

if 'name' in stok :
    print('oui')

print(list(stok.keys()))

print(list(stok.values()))

print(list(stok.items()))

phrase=f"{stok['name']} here"

#=========================================================================:

#EX1
#--------------------1
d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
d['prenom'] = 'Jacques'
print(d)  

#--------------------2
print(list(d.keys()))  

#--------------------3
print(list(d.values()))  

#---------------------4
print(list(d.items()))  

#----------------------5
phrase = f"{d['prenom']} {d['nom']} a {d['age']} ans"
print(phrase)  

#EX2
# Création du dictionnaire stock
stock = {
    "pommes": 50,
    "bananes": 30,
    "oranges": 20,
    "poires": 15
}

# Affichage du dictionnaire pour vérification
print(stock)

# Initialisation du dictionnaire stock
stock = {
    "pommes": 50,
    "bananes": 30,
    "oranges": 20,
    "poires": 15
}

# Ajouter un nouveau produit : "ananas" avec 10 unités en stock.
stock["ananas"] = 10

# Augmenter la quantité de "pommes" de 20 unités.
stock["pommes"] += 20

# Vérifier si "kiwi" est présent dans le stock. S'il ne l'est pas, afficher un message indiquant qu'il est absent.
if "kiwi" not in stock:
    print("Le produit 'kiwi' est absent du stock.")

# Supprimer "oranges" du stock.
del stock["oranges"]

# Afficher la liste des produits disponibles avec leurs quantités
for produit, quantite in stock.items():
    print(f"{produit} : {quantite} unités")


