# Dictionaries (Recnici) su neprimitivni tipovi podataka za skladistenje podataka u 
#  key:value (kljuc:vrednost) paru.

# Recnici su kolekcija koja je:
# uredjena(ordered)
# promenljiva(changeable),
# ne dozoljava duplikate.

# Recnici se zapisuju u viticastim zagradama.

# Recnici mogu sadrzati razlicite tipove podataka.

from enum import auto


automobil = {
    "brend": "Pasat",
    "boja": "bela",
    "godina": 2012,
    "godina": 2020
}

print(automobil)

# Duzina recnika:
duzina = len(automobil)
print(duzina)

# Ukoliko zalimo da prisupimo nekoj vrednosti iz recnika, to mozemo izvrsiti na sledeci nacin:
boja = automobil["boja"]
print(boja)

# 2.nacin
boja = automobil.get("boja")
print(boja)

# Izmena vrednosti:
automobil["godina"] = 2014
print(automobil)

# Dodavanje svojstva i vrednosti se moze izvrsiti na dva nacina:
# 1. nacin
automobil["hp"] = 140
# 2. nacin je koriscenje update() metoda
automobil.update({"hp":140})

print(automobil)

# Brisanje elemenata nekog recnika se moze izvrsiti na dva nacina:
# 1. nacin
#del automobil["hp"]
#print(automobil)
# 2. nacin je koriscenje popitem() metode:
#automobil.pop("hp")

# pop() metoda ako zelimo da izbrisemo poslednji element koristi se popitem() metoda:
automobil.popitem()

# Metoda keys() nam daje kljuceve za dati recnik
print(automobil.keys())

# Metoda values() nam daje kljuceve za dati recnik
print(automobil.values())

# Metoda items() nam vraca listu sacinjenu od tuples(n-torki), gde svaki tuple sadrzi kljuc i vrednost
print(automobil.items())

# Preko del metode mozemo izbrisati ceo recnik:
#del automobil
#print(automobil)

# clear() metoda ce obrisati sve elemente recnika:
automobil.clear()
print(automobil)

automobil = {
    "brend": "Pasat",
    "boja": "bela",
    "godina": 2012
}


# Ispisati vrednosti recnika:
# 1. nacin
for x in automobil.values():
    print(x)
# 2. nacin
for x in automobil:
    print(automobil[x])

# Domaci.
# Napraviti recnik student, koji ce sadrzati sledeca svojstva:
# ime, prezime, broj indeksa, godina_studija, godin_rodjenja, naziv_fakulteta.
# nakon toga izmeniti podatak godina_studija,
# izbrisati naziv_fakulteta,
# dodati novi element prosecna_ocena,
# i na kraju izpisati sve kljuceve  i vrednosti jedne ispod drugih,
# osim godine rodjenja.