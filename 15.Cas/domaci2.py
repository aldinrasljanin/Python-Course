#  Napraviti funkciju gde korisnik unosi dve recenice. Nakon toga ispisati sledece:
#  Duzinu prve i druge recenice,
#  duzinu prve i druge recenice bez eventualnih razmaka na krajevima recenica(strip),
#  pored tih duzina prvu recenicu gde zelimo da zamenimo svaki "a" karakter sa "b" karakterom,
#  drugu recenicu gde zelimo da zamenimo svaki niz karaktera "raspust" sa nizom karaktera "letnji raspust",
#  prvu i drugu recenicu podeljenu na svaki zarez.

#  Napraviti funkciju gde korisnik unosi dve recenice.
def funkcija():
    recenica1 = str(input("Unesite prvu recenicu: "))
    recenica2 = str(input("Unesite drugu recenicu: "))
#  Duzina prve i druge recenice.
    print(f"Duzina prve recenice je: {len(recenica1)}")
    print(f"Duzina druge recenice je: {len(recenica2)}")
#  Duzina prve i druge recenice bez eventualnih razmaka na krajevima recenica.
    skracena_recenica1 = recenica1.strip()
    skracena_recenica2 = recenica2.strip()
    print(len(skracena_recenica1))
    print(len(skracena_recenica2))
#  Pored tih duzina prvu recenicu gde zelimo da zamenimo svaki "a" karakter sa "b" karakterom.
    print(recenica1.replace("a", "b"))
#drugu recenicu gde zelimo da zamenimo svaki niz karaktera "raspust" sa nizom karaktera "letnji raspust"
    print(recenica2.replace("raspust", "letnji raspust"))
#  prvu i drugu recenicu podeljenu na svaki zarez.
    print(recenica1.split(", "))
    print(recenica2.split(", "))
    return(" ")
funkcija()