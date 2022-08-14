# Napraviti recnik student, koji ce sadrzati sledeca svojstva:
# ime, prezime, broj_indeksa, godina_studija, godina_rodjenja, naziv_fakulteta.
# nakon toga izmeniti podatak godina_studija,
# izbrisati naziv_fakulteta,
# dodati novi element prosecna_ocena,
# i na kraju ispisati sve kljuceve i vrednosti jedne ispod drugih,
# osim godine rodjenja.

# Napraviti recnik student
student = {
    "Pme": "Aldin",
    "prezime": "Rasljanin",
    "Broj_indeksa": 00/499,
    "Godina_studija": "prva",
    "Godina_rodjenja": 2005,
    "Naziv_fakulteta": "medicinski"
}
print(student)

# nakon toga izmeniti podatak godina_studija,
student["Godina_studija"] = "druga"
print(student)

# izbrisati naziv_fakulteta
del student["Naziv_fakulteta"]
print(student)

# dodati novi element prosecna_ocena
student["Prosecna_ocena"] = 9
print(student)

# i na kraju ispisati sve kljuceve i vrednosti jedne ispod drugih,
# osim godine rodjenja.
for x,y in student.items():
    if x == "Godina_rodjenja": 
        continue
    print(x,y) 