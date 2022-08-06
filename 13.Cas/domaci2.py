# 2.Napraviti funkciju koja vraca zbir svih elemenata date liste.


lista2 = [1,2,3,4,5]

def zbir_elemenata(lista):
    zbir_elemenata = 0
    for i in lista:
        zbir_elemenata += i 
    return zbir_elemenata

print(zbir_elemenata(lista2))