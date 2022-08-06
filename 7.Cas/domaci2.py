# 2. Proveriti da li uneti broj x pripada intervalu (10,50].
#   Ispisati poruku pripada ili ne pripada.

x = int(input("Unesite jedan broj: "))
# 1.Nacin
if x>10 and x<=50:
    print("Pripada.")
else:
    print(" Ne pripada.")

# 2.Nacin
if x in range(11,51):
    print("Pripada.")
else:
    print(" Ne pripada.")