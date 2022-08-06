#  Danas radimo funkcije

# Funkcija predstavlja blok koda koji ce se izvrsiti samo u slucaju pozivanja.

# sintaksa:
from re import A



def naziv_funkcije():
    # kod za izvrsavanje
    print("Odstampaj nesto.")

naziv_funkcije()

# 1. varijanta je umesto print(...) koristimo rec return

def druga_funkcija():
    # kod za izvrsavanje
    a = 5
    return a

print(druga_funkcija())

# Napraviti funkciju sa nazivom pozdrav koja vraca recenicu "Zdravo svima" na dva nacina.

def pozdrav():
    print("Zdravo svima")
pozdrav()

#def pozdrav2():
    #recenica = "Zdravo svima"
    #return recenica

#print(pozdrav2())

def pozdrav2():
    return "Zdravo svima"
# Nakon return unutar funkcije jedna naredba se vise nece izvrsiti!
# return staviti iskljucivo na kraju
print(pozdrav2())

# Svaka funkcija moze sadrzati parametre (argumente) u sebi koje ce koristiti za izvrsavanje
# odredjenog posla

def vraca_zbir(a,b): # a i b predstavljaju parametre unutar funkcije.
    return a+b

print(vraca_zbir(4,10)) # 4 i 10 predstavljaju argumente.

#  Pozivanjem funkcije moramo staviti onoloko argumenata koliko smo definisali
#  parametara prilikom definisanje funkcije.

def proizvod(x,y):
    return x*y

print(proizvod(4,5))

def proizvod(x,y=10):
    return x*y

print(proizvod(4))

def proizvod(x=5,y=10): # moguce su defaultne vrednosti, ali je njih potrebno definisati kao poslednje.
    return x*y

print(proizvod())

# Napraviti funkciju koja vraca kolicnik dva broja. U slucaju da je delilac jednak nuli imamo poruku
# deljenje nije moguce izvrsiti. Takodje neka delilac ima defaultnu vrednost 1.

def kolicnik(x, y=1):
    if y == 0:
        return"Deljenje nije moguce izvrsiti."
    else:
        return x/y

print(kolicnik(10,2))
print(kolicnik(10,0))
print(kolicnik(10))
# print(kolicnik()) greska jer funkcija obuhvata bar jednu vrednost: x

prom1 = 17
def vrati_prom():
    prom1 = 14
    print(prom1)

vrati_prom()

print(prom1)

#  Promwnjlkiva definisana unutar function scope (prostora funkcije) je vidljiva samo unutar funkcije.
#  Ako je pozovemo van nje, program je nece prepoznati.

def vrati_nesto():
    prom2 = 16
    print(prom2)

# print(prom2) 

# Domaci zadaci:
# 1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata.
#    Odnosno povrsinu kvadrata ako su dva data argumenta jednaka.

# 2. Napraviti funkciju koja pretvara broj inche u cm.
#    Pozivanjem funkcije treba uneti broj incha.