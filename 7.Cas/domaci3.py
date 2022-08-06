# 3. Korisnik unosi dva realna broja x i y. Napisati program koji izracunava i stampa,
#   kolicnik (x:y) ako je broj y razlicit od nule, a inace ispisuje poruku deljenje je nemoguce.

x = float(input("Unesite prvi realan broj: "))
y = float(input("Unesite drugi realan broj: "))

if y != 0:    # if y == 0:
    print(f"Kolicnik dva uneta broja je {x / y}")
else:
    print("Deljenje je nemoguce.")