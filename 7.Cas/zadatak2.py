# 2. Napisati program koji, ako je uneti broj veci od 0, stampa poruku broj je pozitivan.
# Obuhvatiyi i slucajeve kad je broj manji od nule i jednak nuli.

x = int(input("Unesite neki broj: "))

if x>0:
    print("Broj je pozitivan.")
elif x<0:
    print("Broj je manji od nule.")
else:
    print("Broj je jednak nuli.")