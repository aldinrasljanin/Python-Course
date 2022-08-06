# extend() metoda nam mogucava spajanje dve liste

voce = ["jabuka", "tresnja", "banana"]
tropsko = ["mango", "ananas"]

voce.extend(tropsko)

print(voce)

# extend() metoda pored liste moze dodati i tuple, set, dictionaries...

voce = ["jabuka", "tresnja", "banana"]
tropsko = {"mango", "ananas"}

voce.extend(tropsko)

print(voce)

# pop() metoda sluzi za brisanje elemenata liste.
# Mozemo izbrisati specificni element (dodavanjem indeksa kao argument metode),
# ili poslednji element liste (izostavljajuci argument metode).

voce.pop(2)
print(voce)

izbrisana_stavka = voce.pop() # mozemo sacuvati kao promenjljivu izbrisanu stavku iz liste
print(voce)

print(izbrisana_stavka)

# del keyword
# del mozemo koristiti za brisanje odredjenog elementa liste kao i brisanje kompletne liste

# Brisanje elementa liste
del voce[0]
print(voce)

# Brisanje cele liste
del voce

# clear() metoda sluzi za brisanje svih elemenata liste

voce = ["jabuka", "tresnja", "banana"]
print(voce)
voce.clear()
print(voce)

# Ispisati elemnte liste jedan ispod drugog, gde je drugo slovo elementa a
lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]

for i in (lista):
    if i[1]=="a":
        print(i)

# Saciniti lista2 da bude od istih elemenata kao i lista1
lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []




for i in lista1:
    lista2.append(i)

print(lista2)

# 2.nacin
lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []

lista2 = [i for i in lista1]
print(lista2)

# jos jedan primer
lista1 = ["ananas", "banana", "kruska", "dinja"]
lista2 = []

lista2 = [i for i in lista1 if i[-1]=="a"]
print(lista2)

# napraviti listu od elemenata od 1-10, na nacin kakav smo radili u prethodnom primeru

lista3 = [i for i in range(1,11) ]
print(lista3)

# samo parni brojevi
lista4 = [i for i in range(1,11) if i%2==0]
print(lista4)

# Napraviti novu listu sacinjenu od elemenata lista5 samo u slucaju da naidjemo na "banana" ispisati "narandza"
lista5 = ["ananas", "banana", "kruska", "dinja"]

lista6 = [i if i!="banana" else "narandza" for i in lista5] 
print(lista6)

# Zakljucak.
# Ako imamo jedan uslov onda cemo ispisati na sledeci nacin:
#  lista2 = [i for i in lista1 if i[-1]=="a"]
# Ako imamo vise uslova onda cemo ispisati na sledeci nacin:
#  lista6 = [i if i!="banana" else "narandza" for i in lista5] 

# Domaci:
# napraviti dve liste po svojoj zelji nek imaju po 5 elemenata.
# dodati drugu listu prvoj,
# izbrisati prvi i poslednji element prosirene liste,
# napraviti novu listu koja ce biti sadrzana od onih elemenata poslednje uredjene liste,
# za koje vazi da je prvi karakter = "a",
# napraviti jos jednu listu koju cine elementi poslednje izmenjene liste ali da svi budu ispisani 
# velikim slovom.(upper)