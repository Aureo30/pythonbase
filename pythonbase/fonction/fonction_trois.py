# cree une fonction max() qui renvoit le résultat le plus haut entre 2 valeurs

def max(a, b):
    if a > b:
        return a
    else:
        return b


first_value = int(input("Entrer la première valeur "))

two_value = int(input("Entrer la deuxième valeur "))

max_value = max(first_value, two_value)
print("la valeur max est : ", max_value)