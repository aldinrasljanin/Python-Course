#  Stringovi

# Pristupanje odredjenom elementu stringa
a = "Hello World!"
print(a[0])         # Pristupanje prvom karakteru stringa
print(a[len(a)-1])  # Pristupanje poslednjem karakteru stringa(prvi nacin)
print(a[-1])        # Pristupanje poslednjem karakteru stringa(drugi nacin)

# listanje elemenata jedan ispod drugog
for i in "car":
    print(i)

# metoda koja vraca duzinu stringa:
b = "Danas je suncan dan."
duzina = len(b)
print(duzina)

# Ispitivanje clanstva:
b = "Danas je suncan dan."
# Proveriti da li se u promenjljivoj b nalazi rec "suncan"

if "suncan" in b:
    print("Rec suncan se nalazi u datoj recenici.")
else:
    print("Rec suncan se ne nalazi u datoj recenici.")

# Ispitajte da li se rec "expensive" ne nalazi u sledecoj recenici:
c = "The best things in life are free."

if "expensive" not in c:
    print("Rec expensive se ne nalazi u datoj recenici.")
else:
    print("Rec expensive se nalazi u datoj recenici.")


# Slicing(secenje) stringa

c = "The best things in life are free."

print(c[4:15])  # best things
print(c[-5:-1]) # free

# Uzimanje dela stringa od odredjenog indeksa pa do kraja:
print(c[4:])

# Uzimanje dela stringa od pocetka do odredjenog indeksa:
print(c[:15])

# primer
print(c[-14:-10])


# Spajanje strigova:
a = "Danas je "
b = "Suncan dan."
print(a + b)              # 1.Nacin
print(a, b)               # 2.Nacin
print(f"{a}{b}")          # 3.1. Nacin (format metoda)
print("{}{}".format(a,b)) # 3.2. Nacin (format metoda)

# Pretvaranje celog stringa u velika slova:
c = "The best things in life are free."
print(c.upper())    # SINTAKSA JE "string".naziv_metode()

# Pretvaranje celog stringa u mala slova:
c = "The best things in life are free."
print(c.lower())    # SINTAKSA JE "string".naziv_metode()

# Domaci zadatak.
# Napraviti funkciju koja od korisnika trazi unos recenice.
#  Funkcija treba da vrati datu recenicu u sledecim oblicima:
#  Recenica ispisana velikim slovima,
#  Recenica ispisana malim slovima,
#  Duzinu unete recenice.