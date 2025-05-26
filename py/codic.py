
a = int(input("Saisissez le premier nombre entier a : "))
b = int(input("Entrez le deuxième nombre entier b : "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a  

print(f"Le PGCD de {a} et {b} est : {gcd(a, b)}")


rita='locale host'
pop=64563
catir='fif bom'
