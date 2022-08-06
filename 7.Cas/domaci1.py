# 1. Napisati program kojim se unose dva pozitivna cela broja a i b. Napisati program
#   koji izracunava i stampa povrsinu kvadrata ako su uneti brojevi jednaki, 
#   odnosno povrsinu pravougaonika ako su brojevi razliciti.
#   Uneti brojevi predstavljaju stranice pravougaonika odnosno kvadrata.

a = int(input("Unesite prvi ceo pozitivan broj: "))
b = int(input("Unesite drugi ceo pozitivan broj: "))

if a == b:
    print(f"Povrsina kvadrata je {a**2}.")
else:
    print(f"Povrsina pravougaonika je {a * b}.")