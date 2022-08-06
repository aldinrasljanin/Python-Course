# Domaci zadatak. Koristeci input() metoda i format() metoda odraditi sledece.
# Traziti od korisnika da unese broj godina, visinu i tezinu. Nakon toga napraviti novu promenjlivu
# koja ce biti string unutar kog ce se nalaziti 3 unete vrednosti i koja ce lepo izgledati.

broj_godina = int(input("Unesite broj svojih godina: "))
visina = int(input("Unesite svoju visinu : "))
tezina = int(input("Unesite svoju tezinu : "))
print(broj_godina, visina, tezina)

Korisnik = "Aldin"
naziv_kursa = "Python"
broj_godina = 17

nova_varijabla = f"Cao, moje ime je {Korisnik}.Ucenik sam {naziv_kursa} kursa i imam {broj_godina} godina."
print(nova_varijabla)
print(type(nova_varijabla))