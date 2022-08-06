# 3. Zadatak:
#   Napisat sve one brojeve koji su deljivi sa 3 iz intervala (1,201).


for i in range(1,201,1):
    if i%3 == 0:
        print(i)