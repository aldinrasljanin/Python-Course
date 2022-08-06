#  1. Zadatak:
#  Napraviti dva niza od po 6 elementa. Neka se izvrsi iteracija tako da
#  se element prvog niza prikaze onoliko koliko ima elemenata drugog niza
#  a pritom se svaki element drugog niza(ugnjezdava for petlja).

Prvi_niz = [1,2,3,4,5,6]
Drugi_niz = ["jedan","dva","tri","cetiri","pet","sest"]

for a in Prvi_niz:
    for b in Drugi_niz:
        print(a,b)