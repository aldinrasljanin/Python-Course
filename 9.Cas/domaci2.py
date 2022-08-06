#  2. Zadatak:
#  Ispisati sve parne prirodne brojeve od 10 do 110 (ukljucujuci oba) izuzev
#  16,22,44,66,88,102,108

for a in range(10,111):
    if a%2 == 0:
        if a == 16:
            continue
        elif a == 22:
            continue
        elif a == 44:
            continue
        elif a == 66:
            continue
        elif a == 88:
            continue
        elif a == 102:
            continue
        elif a == 108:
            continue
        print(a)

# Drugi nacin
# if i == 16 or i == 22 or i == 44 or i == 66 or i == 88 or i == 102 or i == 108:
# continue
#print (i)