# 1. Napisati program koji proverava da li je uneti ceo broj x paran ili nepaaran 
# i ispisuje odgovarajucu poruku.

x = int(input("Unesite ceo broj: "))

if x % 2 == 0:
    print("Uneti broj je paran.")
else:
    print("Uneti broj je neparan.")
