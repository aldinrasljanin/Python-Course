# Kroz interaciju date liste ispisati "BANANA" za svaki element osim gde se nadje "dinja".


lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]

lista2 = [i if i == 'dinja' else "BANANA" for i in lista]
print(lista2)

# Sortiranje liste: sort()

lista = ["kajsija", "jabuka", "ananas", "banana", "kruska", "dinja"]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# Sortitanje prema brojevima:

lista2 = [54, 78, -24, 65, -91, 0]

lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

# Po defaultu sort() metoda je case sensitive (prednost imaju velika slova).

lista = ["Kajsija", "jabuka", "Ananas", "banana", "Kruska", "dinja"]
lista.sort()
print(lista)

# U slicaju da zelimo ukinuti prednost velikih slova u odnosu na mala, to mozemo uciniti na sledeci nacin:

lista = ["Kajsija", "jabuka", "Ananas", "banana", "Kruska", "dinja"]

lista.sort(key=str.lower)
print(lista)

# reverse() metoda sluzi za vracanje liste obrnutim redosledom u zavisnosti od redosleda pisanja elementa u listi.

lista = ["kajsija", "jabuka", "ananas", "banana", "kruska", "dinja"]
lista.reverse()
print(lista)

# Primer sa brojevima:

lista2 = [54, 78, -24, 65, -91, 0]
lista2.reverse
print(lista2) 