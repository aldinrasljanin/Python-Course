# 3. Napisati program koji, proverava da li je zbir dva uneta broja deljiv sa 3 ili nije
# i ispisati poruku jeste ili nije

x = int(input("Unesite prvi broj: "))
y = int(input("Unesite drugi broj: "))

if (x+y)%3 == 0:
    print("Zbir dva broja je deljiv sa tri.")
else:
    print("Zbir dva broja nije deljiv sa tri.")
