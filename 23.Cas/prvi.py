student = {
    "Pme": "Dzenan",
    "prezime": "Kosuta",
    "Godina_rodjenja": 1997,
    "Broj_indeksa": 119141,
    "Naziv_fakulteta": "DUNP"
}
print(student)
# Nije dobra praksa. Jer student2 je samo referenca na recnik student.
student2 = student
print(student2)

student2["Broj_indeksa"] =256325
print(student)
print(student2)

# Postoje 2 nacina za kopiju recnika:
# 1. Nacin
student = {
    "Pme": "Dzenan",
    "prezime": "Kosuta",
    "Godina_rodjenja": 1997,
    "Broj_indeksa": 119141,
    "Naziv_fakulteta": "DUNP"
}
student2 = student.copy()
print(student2) 
student2["Broj_indeksa"] = 256325
print(student2)
print(student) 

# 2. Nacin
student = {
    "Pme": "Dzenan",
    "prezime": "Kosuta",
    "Godina_rodjenja": 1997,
    "Broj_indeksa": 119141,
    "Naziv_fakulteta": "DUNP"
}
student2 = dict(student)
print(student2)
student2["Broj_indeksa"] = 256325
print(student2)
print(student) 

# Nested (ugnjezdeni) recnici
# Dozvoljeno je unutar nekog recnika kao vrednost staviti novi recnik.
student = {
    "Pme": "Dzenan",
    "prezime": "Kosuta",
    "Godina_rodjenja": 1997,
    "Broj_indeksa": 119141,
    "Fakultet": {"naziv": "DUNP", "lokacija": "Vuka Karadzica 49", "ocenjen": 6.7},
    "Ocene_prema_godinama": [6,7,8,9]
}
print(student) 