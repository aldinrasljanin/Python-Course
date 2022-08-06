# Booleans
# Booleans nam predstavlja jednu od dve vrednosti:
# 1. True, ili
# 2. False

print(2>5)
print(10<=10)
print(8==-8)
print(7!=7)

# Funkcija bool() nam omogucava da ispitamo logicku vrednost neke stvari.

print(bool(" da li je 2 vece od 5"))
print(bool(""))

# Bilo koji string koji nije prazan("") ce da vrati True. Jedino prazan string vraca False.

print(bool(" ")) # Samo prazan string vraca False!!!

print(bool(7))
print(bool(-7))
# Bilo koji broj razlicit od nule nam vraca True. Jedino 0 vraca False.

print(bool(0))
print(bool("0")) # Vraca True zato sto je u pitanju string koji nije prazan.

print(bool(7>9))

# Svaka lista, tuple, set(skup), dictionary(recnik) ce vratiti True osim praznih.

print(bool([1,2,3]))
print(bool([]))