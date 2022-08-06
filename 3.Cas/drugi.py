# Dedeljivanje jedne vrednosti za vise promenjljivih:

# 1 Nacin

kurs1 = "Kurs programskog jezika Python"
kurs2 = "Kurs programskog jezika Python"
kurs3 = "Kurs programskog jezika Python"

print(kurs1, kurs2, kurs3)

# 2 Nacin

kurs_prvi, kurs_drugi, kurs_treci = "Prvi kurs", "Drugi kurs", "Treci kurs"

print(kurs_prvi, kurs_drugi, kurs_treci)

# Pozivanje prilikomm printa:

x = "Danas je lepo vreme"

y = "Sutra ce biti kisovito"

# 1. Nacin
print(x,y)

# 2. Nacin
print(x + ". " + y+ ".")

# Ako spajanje izvrsavamo putem operatora + mozemo da dobijemo error u sledecim slucajevima:

a = "Danas sam dobio "
b = 5
#print(a + b)

# U Pythonu ne mozemo izvrsiti spajanje (Putem operatora +) razlicitih tipova podataka!!!

print (a, b,".") 


# Domaci zadatak. 
# Dodeliti 5 razlicitih vrednosti za 5 promenjljivih razlicitog naziva (Neka u tih 5 promenljivih budu koristene
# razlicite metode dodeljivanja vrednosti) i izvrsiti spajanje dve ili tri promenljive, kao i 
# print tipa svake od tih promenljivih.