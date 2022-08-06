#  3. Zadatak:
#  Ispisati sve elemente prethodno definisane liste od 10 elemenata odpozadi.

Lista1 = [1,2,3,4,5,6,7,8,9,10]

duzina = len(Lista1)
print(duzina)

for a in range(duzina - 1,-1,-1):
    print(Lista1[a])