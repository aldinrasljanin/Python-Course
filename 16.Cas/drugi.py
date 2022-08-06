# Radno vreme jedne organizacije je izmedju 9 i 17 casova.
# Odrediti da li je mejl stigao u toku radnog vremena.
# 9 spada u radno vreme, dok 17h ne spada.

def funkcija():
    sat = int(input("Unesite sat prispeca mejla: "))
    minut = int(input("Unesite minut prispeca mejla: "))
    if sat in range(9,17):
        print("Da")
    else:
        print("Ne")

funkcija()

# Domaci zadatak.
# Koristeci bool funkciju ispitati sledece stvari:
# 1. Da li je string koji je uneo korisnik True ili False.
# 2. Da li je broj koji je uneo korisnik True ili False.
# 3. Da li je lista1 True ili False. lista1 = [0]
# 4. Uporediti dva uneta broja od strane korisnika.