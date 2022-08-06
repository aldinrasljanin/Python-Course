# 1.Napraviti funkciju koja ispisuje vrednosti date liste pored indeksa, jedne ispod drugih.

lista1 = ["Audi", "BMW", "Mercedes", "Golf", "Yugo", "Ferari"]

def vred_liste(lista):
    for i in range(0,len(lista)):
        print(i,lista[i])
    return "To su bili elementi nase liste sa svojim indeksima."

print(vred_liste(lista1))