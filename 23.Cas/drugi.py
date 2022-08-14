import datetime

trenutno_vreme = datetime.datetime.now()
print(trenutno_vreme)

datum_rodjenja = datetime.datetime(2005,5,9, 9,15,47)
print(datum_rodjenja)

dan_rodjenja = datum_rodjenja.strftime("%a")
print(dan_rodjenja)

mesec_rodjenja = datum_rodjenja.strftime("%B")
print(mesec_rodjenja)

datum2= datetime.datetime(2005, 5, 9)
print(datum2) 