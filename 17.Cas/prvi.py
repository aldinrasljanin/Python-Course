# Liste
# Elementi unutar liste su:
# poredjani,
# promenjljivi,
# dozvoljavaju duplikate.

# U drugim programskim jezicima liste se nazivaju nizovima (Array).

# Liste u Pythonu mogu sadrzati razlicite tipove podataka:
lista1 = ["Ensar", "Hana", "Vahid", 17, 16, 17] 
print(lista1)

duzina1 = len(lista1)
print(duzina1)

lista2 = ["Aldin", "Davud", 17, 17, True, False, [1,2,3], ("abc")]
print(lista2)

# Pristupanje elementima
print(f"{lista1[1]} ima {lista1[-2]} godina.")
print(f"Tvrdnja da {lista2[1]} ima {lista2[3]} godina je {lista2[4]}.")

# Menjanje vrednosti nekog elementa liste:
voce = ["breskva", "bostan", "kajsija", "dinja", "banana"]
print(voce)

voce[2]= "kivi"
print(voce)

voce[2:] = "ananas", "jagoda", "jabuka"
print(voce)

voce[2:] = "kruska", "sljiva", "narandza", "grejpfruit", "mango", "smokva"
print(voce)

# Liste su promenjljive. Mozemo izmeniti odredjeni element liste pristupanjem njemu preko indeksa.
# Svakako mozemo izmeniti vise elemenata od jednom. Takodje nam je dozvoljeno da ovakvim izmenama 
# prosirimo nasu liste sve spomenuto je odradjeno u primerima iznad.

# Insert() metoda nam sluzi za dodavanje elementa listi na tacno odredjenom indeksu.
voce = ['breskva', 'bostan', 'kruska', 'sljiva', 'narandza', 'grejpfruit', 'mango', 'smokva']
voce.insert(1, "nar")
print(voce)

# append() metoda nam sluzi za dodavanje elementa na kraju liste.
voce.append("jabuka")
print(voce)

# Domaci:
lista1 = ["Mercedes", "Audi","Fiat", "Porse", "Pasat"]
lista2 = [2008, 2014, 2002, 2019, 2005]
# Uporediti duzine prve i druge liste,
# dodati u prvoj listi na prvoj pocetnom indeksu "BMW"
# zatim dodato godinu tog automobila na istoj poziciji, ali u drugoj listi
# izmeniti poslednaj dva elementa sa neka druga dva (za obe liste),
# nakon svega dodati u obe liste kao poslednji element neku listu 
# sa po 3 elementa razlicitih tipova podataka.                                                                                                              