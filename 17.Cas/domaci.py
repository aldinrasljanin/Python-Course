# Uporediti duzine prve i druge liste,
# dodati u prvoj listi na prvoj pocetnom indeksu "BMW"
# zatim dodato godinu tog automobila na istoj poziciji, ali u drugoj listi
# izmeniti poslednja dva elementa sa neka druga dva (za obe liste),
# nakon svega dodati u obe liste kao poslednji element neku listu 
# sa po 3 elementa razlicitih tipova podataka.  

lista1 = ["Mercedes", "Audi","Fiat", "Porse", "Pasat"]
lista2 = [2008, 2014, 2002, 2019, 2005]
# Uporediti duzine prve i druge liste
duzina1 = (len(lista1))
duzina2 = (len(lista2))
if bool(duzina1>duzina2):
    print("Prva lista je duza od druge liste.")
elif bool(duzina1<duzina2):
    print("Prva lista je kraca od druge liste.")
else:
    print("Obe liste su iste duzine.")
# dodati u prvoj listi na prvom pocetnom indeksu "BMW"
lista1.insert(0, "BMW")
print(lista1)
# zatim dodati godinu tog automobila na istoj poziciji, ali u drugoj listi
lista2.insert(0, 2020)
print(lista2)
# izmeniti poslednja dva elementa sa neka druga dva (za obe liste)
lista1[4:] = "Golf", "Lada"
print(lista1)
lista2[4:] = 2003, 1979
print(lista2)
# nakon svega dodati u obe liste kao poslednji element neku listu 
# sa po 3 elementa razlicitih tipova podataka.
lista1.append(["jagoda", 7, True ])
print(lista1)
lista2.append(["Python", 2.5, False])
print(lista2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             