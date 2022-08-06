# Napraviti funkciju koja od korisnika trazi unos recenice.
#  Funkcija treba da vrati datu recenicu u sledecim oblicima:
#  Recenica ispisana velikim slovima,
#  Recenica ispisana malim slovima,
#  Duzinu unete recenice.

def funkcija():

    recenica = str(input("Unesite recenicu: "))

    print(recenica.upper())
    print(recenica.lower()) 
    print(len(recenica))
    return(" ")

print(funkcija())