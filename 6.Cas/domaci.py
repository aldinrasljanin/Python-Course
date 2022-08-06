#Domaci zadatak. Traziti od korisnika unos 4 broja.
# Zatim izvrsiti poredjenje zbira prva dva broja sa zbirom druga dva broja.
# Nakon poredjenja zbira izvrsiti poredjenje razlike.

# Traziti od korisnika unos 4 broja.
Prvi_broj = int(input("Unesite prvi broj: "))
Drugi_broj = int(input("Unesite drugi broj: "))
Treci_broj = int(input("Unesite treci broj: "))
Cetvrti_broj = int(input("Unesite cetvrti broj: "))

# Poredjenje zbira prva dva broja sa zbirom druga dva broja.
Zbir1 = Prvi_broj + Drugi_broj
Zbir2 = Treci_broj + Cetvrti_broj
print(f"Zbir brojeva {Prvi_broj} i {Drugi_broj} je {Zbir1}.")
print(f"Zbir brojeva {Treci_broj} i {Cetvrti_broj} je {Zbir2}.")

if Zbir1>Zbir2:
    print(f"Zbir brojeva {Prvi_broj} i {Drugi_broj} je veci.")
elif Zbir1<Zbir2:
    print(f"Zbir brojeva {Treci_broj} i {Cetvrti_broj} je veci.")
else:
    print(f"Zbir brojeva su jednaki.")

# Poredjenje razlike
Razlika1 = Prvi_broj - Drugi_broj
Razlika2 = Treci_broj - Cetvrti_broj
print(f"Razlika brojeva {Prvi_broj} i {Drugi_broj} je {Razlika1}.")
print(f"Razlika brojeva {Treci_broj} i {Cetvrti_broj} je {Razlika2}.")

if Razlika1>Razlika2:
    print(f"Razlika brojeva {Prvi_broj} i {Drugi_broj} je veca.")
elif Razlika1<Razlika2:
    print(f"Razlika brojeva {Treci_broj} i {Cetvrti_broj} je veca.")
else:
    print("Razlike brojeva su jednake.")