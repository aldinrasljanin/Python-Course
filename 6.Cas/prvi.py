# Kondicionali.
# if, elif i else...

# sintaksa:
#if a>b:
#    print(a," je vece od ",b)
#    print("vece od")

# Pravilo indentation(razmaka). Izvrsavanje koda nekog nakon neke naredbe u Pythonu se mora
# vrsiti pod razmacima(bar jedan razmak).
# Ako imamo vise linija izvrsavanja neophodno je da svaka linija ima prethodno jednak broj razmaka.




a = 4
b = 45

if a>b:
    print(f"{a} je vece od {b}")
elif a==b:
    print(f"{a} je jednako {b}")
else:
    print(f"{a} je manje od {b}.")

# Primer1. 2.Nacin

print(f"{a} je vece od {b}") if a>b else print(f"{a} je jednako {b}") if a==b else print(f"{a} je manje od {b}.")

# Zadatak1. Ako a iznosi 4, b isnosi 9. Izvrsiti print zbir brojeva a i b je veci ili manji od 12.
#  Razlika brojeva b i a veca ili manja od 6.

a = 4
b = 9

if b+a>12:
    print(f"Zbir brojeva {a} i {b} je veci od broja 12.")
elif a+b<12:
    print(f"Zbir brojeva {a} i {b} je manji od broja 12.")
else:
    print(f"Zbir brojeva {a} i {b} je jednak broju 12.")

a=4
b=9

if b-a>6:
    print(f"Razlika brojeva {b} i {a} je veci od broja 6.")
elif b-a<6:
    print(f"Razlika  brojeva {b} i {a} je manja od broja 6.")
else:
    print(f"Razlika  brojeva {b} i {a} je jednaka broju 6.")

#Domaci zadatak. Traziti od korisnika unos 4 broja.
# Zatim izvrsiti poredjenje zbira prva dva broja sa zbirom druga dva broja.
# Nakon poredjenja zbira izvrsiti poredjenje razlike.