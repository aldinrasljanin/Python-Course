# for i in range(10,0,-1):
# print(i)


#  6. primer(Iteracija kroz listu)
lista1 = ["tastatura", "mis", "maticna ploca", "graficka kartica", "procesor"]
for komp in lista1:
    print(komp)

#  7. (Nested for loop - Ugnjezdene for petlje)
lista1 = [1,2,3,4,5]
lista2 = ["tastatura", "mis", "maticna ploca", "graficka kartica", "procesor"]
for i in lista1:
    for j in lista2:
        print(i,j)


# sintaksa za pristup odredjenom elementu iterirajuce promenljive
recenica = "Danas je suncan dan."
# pronadji prvi karakter nase recenice:
prvi = recenica[0]
print(prvi)
print(recenica[6])
# Izvuci iz lista2 maticnu plocu
print(lista2[2])

# Pomocu ugradjene funkcije len() mozemo dobiti duzinu liste.
duzina = len(lista2)
print(duzina)

# Takodje mozemo dobirti duzinu stringa pomocu funkcije len().
duzina_rec = len(recenica)
print(duzina_rec)

# 8.prime
for i in range(0,len(lista2)):
    #print(i) ovako dobijamo indekse nase liste
    #print(lista2[i]) ovako dobijamo elemente nase liste
    print(i,lista2[i]) # Izvrsili smo print indekse i elemente tom indeksu

# 9.primer
for i in recenica:
    print(i)

# 10.primer
for i in range(0,len(recenica)):
    print(i, recenica[i])

#  Dve nove naredbe:
#  1.  break    => zapravo predstavlja prekid iteracije ako je odredjeni uslov zadovoljen
#  2.  continue => predstavlja da se "zaobidje" odredjeni element ako je pod uslovom

# 11.primer
for i in lista2:
    if i == "mis":
        break
    print(i)

# 12.primer
for i in lista2:
    if i == "mis":
        continue
    print(i)

#Domaci zadatak:

#  1. Zadatak:
#  Napraviti dva niza od po 6 elementa. Neka se izvrsi iteracija tako da
#  se element prvog niza prikaze onoliko koliko ima elemenata drugog niza
#  a pritom se svaki element drugog niza(ugnjezdava for petlja). # primer7

#  2. Zadatak:
#  Ispisati sve parne prirodne brojeve od 10 do 110 (ukljucujuci oba) izuzev
#  16,22,44,66,88,102,108

#  3. Zadatak:
#  Ispisati sve elemente prethodno definisane liste od 10 elemenata odpozadi.