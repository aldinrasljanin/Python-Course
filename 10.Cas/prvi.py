#  2. while petlja
#  sintaksa

# 1.primer
i=4
while i<10:
    print(i)
    i += 1  # (i = i + 1)

# 2.primer
i = 10
while i <= 20:  # and i%2 == 0:
    print(i)
    i += 2 
else:
    print("Izvrsili smo ispis parnih brojeva od 10 do 20.")

# 3.primer
i=str(input("Unesite kako je vreme danas: "))
while i != "Suncan dan":
    print(i)
    i=str(input("Unesite kako je vreme danas: "))



# Domaci:
# 1.Koristiti while petlju gde ce korisnik unositi prirodne brojeve
#   i oni ce se ispisivati sve do momenta kada korisnik unese broj 149

# 2.Ispisati sve elemente kao i indekse (element,indeks na kom se nalazi element) 
#   prethodno definisane liste od 10 elemenata odpozadi.