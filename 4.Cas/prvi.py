
my_var = 5
MyVar = 4
myVar = 3


# Upotreba format() metode za umetanje promelnjivih unutar teksta.
# 1. Nacin koriscenja format metode
print("Na kontrolnom zadatku sam dobio {}". format(MyVar))

prvi_iznos = 200
drugi_iznos = 160
treci_iznos = 40
nova_recenica = "Danas sam u prodavnici kupio litar ulja, kojeg sam platio {} dinara. \
Medjutim prosle nedelje je ulje kostalo {} dinara, sto znaci da je poskupelo, \
za {} dinara.".format(prvi_iznos, drugi_iznos, treci_iznos)
print(nova_recenica)

# 2. Nacin koriscenja format metode

print(f"Na kontrolnom zadatku sam dobio {MyVar}")

nova_recenica2 = f"Danas sam u prodavnici kupio litar ulja, kojeg sam platio {prvi_iznos} dinara. \
Medjutim prosle nedelje je ulje kostalo {drugi_iznos} dinara, sto znaci da je poskupelo, \
za {treci_iznos} dinara."

print(nova_recenica2)