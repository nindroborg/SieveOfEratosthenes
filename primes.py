import datetime
from datetime import timedelta
import math
import primelib


prime_max = 50000

def get_time():
    return datetime.datetime.now()

# METHODE V1: Entfernen aller Vielfachen von 2 bis Wurzel prime_max 
# mit .remove methode für Listen
def get_primes_V1(max):
    sieve = list(range(max+1))
    sieve.remove(0)
    sieve.remove(1)

    for x in range(2, round(math.sqrt(max))):
        t = 2
        while x * t <= max:
            num = (x * t)
            # print(x, t, num)
            t += 1
            
            try:
                sieve.remove(num)
            except:
                continue

    return sieve


# METHODE V2: Entfernen aller Vielfachen von 2 bis Wurzel prime_max 
# mit .remove methode für Listen, jedoch ohne Vielfache gerader Zahlen außer 2
def get_primes_V2(max):
    sieve = list(range(max+1))
    sieve.remove(0)
    sieve.remove(1)

    to_test = list(range(3, round(math.sqrt(max)), 2))
    to_test.insert(0, 2)  # "2" am Anfang der Liste zufügen

    for x in to_test:
        t = 2
        while x * t <= max:
            num = (x * t)
            # print(x, t, num)
            t += 1
            
            try:
                sieve.remove(num)
            except:
                continue

    return sieve


# METHODE V3: Kennzeichnen aller Veilfachen von 2 bis Wurzel prime_max in sieve mit 'x'
# ohne Iterierung über Vielfache gerader Zahlen außer 2. Am Schluß einmaliges 
# iterieren der sieve  Liste und umkopieren der übrig gebliebenen Zahlen (Primzahlen)  
# in eine neue liste prime_list
def get_primes_V3(max):
    sieve = list(range(max+1))
    sieve[0]='x'
    sieve[1]='x'

    to_test = list(range(3, round(math.sqrt(max)), 2))
    to_test.insert(0, 2)  # "2" am Anfang der Liste zufügen

    for x in to_test:
        t = 2
        while x * t <= max:
            num = (x * t)
            # print(x, t, num)
            t += 1
            
            try:
                sieve[num]='x'
            except:
                continue

    primes_list = []
    for prim in sieve:
        if prim != 'x':
            primes_list.append(prim)

    return primes_list

# METHODE V4 (SCHNELLSTE VARIANTE!): Kennzeichnen aller Veilfachen von 2 bis Wurzel prime_max in sieve mit 'x'
# dabei werden nur Vielfache von noch existenten Zahlen (Prim!) aus der sieve Liste selbst genommem.  
# Am Schluß einmaliges iterieren der sieve  Liste und umkopieren der übrig gebliebenen   
# Zahlen (Primzahlen) in eine neue liste prime_list 
def get_primes_V4(max):
    sieve = list(range(max+1))
    sieve[0]='x'
    sieve[1]='x'

    for x in sieve:
        if x == 'x':
            continue
        elif x > round( math.sqrt(max) ):
            break
        
        t = 2
        while x * t <= max:
            num = (x * t)
            # print(x, t, num)
            t += 1
            
            try:
                sieve[num]='x'
            except:
                continue

    primes_list = []
    for prim in sieve:
        if prim != 'x':
            primes_list.append(prim)

    return primes_list

# METHODE V5: Vergleich mit der Sieb des Erathostenes Implementation aus der primlib Bibliothek von Github
def get_primes_V5(max):
    return primelib.sieveEr(max)

# METHODE V6: Vergleich mit der Sieb des Erathostenes Implementation aus der primlib Bibliothek von Github
def get_primes_V6(max):
    return primelib.getPrimeNumbers(max)


def report_prim_calc(primes_list, duration, max_prime, method):
    print("\n",len(primes_list)," Primzahlen bis ", max_prime, " nach ", method, ": ", passed_time, " Sekunden\n\n")

# Version 1
timestamp_begin = get_time()
primes_V1 = get_primes_V1(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V1, passed_time, prime_max, "V1")

# Version 2
timestamp_begin = get_time()
primes_V2 = get_primes_V2(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V2, passed_time, prime_max, "V2")

# Version 3
timestamp_begin = get_time()
primes_V3 = get_primes_V3(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V3, passed_time, prime_max, "V3")

# Version 4
timestamp_begin = get_time()
primes_V4 = get_primes_V4(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V4, passed_time, prime_max, "V4")

# Version 5
timestamp_begin = get_time()
primes_V5 = get_primes_V5(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V5, passed_time, prime_max, "V5")

# Version 6
timestamp_begin = get_time()
primes_V6 = get_primes_V6(prime_max)
timestamp_end = get_time()
passed_time = timedelta.total_seconds(timestamp_end-timestamp_begin)
report_prim_calc(primes_V6, passed_time, prime_max, "V6")



