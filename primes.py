# primes.py
# erzeuge der Primzahl von 1 bis 1000

for n in range(2, 1001):
    for x in range(2, n):
        if n % x == 0:         
            break
    else:
        print (n) 