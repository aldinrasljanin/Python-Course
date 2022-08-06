# Math

from cmath import sqrt
import math


x = min(1,4,-28,65)
print(x)

x = max(1,4,-28,65)
print(x)

# abs() metoda vraca apsolutnu vrednost broja.

x = 28
y = -32

print(abs(x))
print(abs(y)) 



# pow() metoda sluzi za stepenovanje brojeva
# Prvi argument predstavlja osnovu
# Drugi argument predstavlja stepen

x = pow(2, 3)
print(x)

# Za neke naprednije metode moramo izvrsiti import math

x = math.sqrt(9) # math.sqrt je koren broja
print(x)

x = 12.4
y = 13.8

z = math.ceil(x) # ide do prvog veceg celog broja
w = math.floor(y) # ide do prvog manjeg celog broja
print(z)
print(w)

pii = math.pi 

print(pii) 