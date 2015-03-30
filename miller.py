# implements the MIller-Rabin primality test on integers

from random import randint
from math import log

n = int(raw_input("Input the number to be tested : "))

if n % 2 == 0 or n % 5 == 0:
    print('Hope you\'re kidding...\n')
    exit()

witnesses = [2,3,5,7,11,13,17,19,23]

phin = n - 1
s = 0
d = phin
while d % 2 == 0:
    d /= 2
    s += 1


bound = phin if phin < 41 else 41
if int(log(n,2)) < 61:
    bound = 9
used = []
x = 0

for i in range(1, bound):
    if bound > 9:
        x = randint(2, phin)
        while x in used:
            x = randint(2, phin)
    else:
        x = witnesses[i-1]
    if pow(x, phin, n) != 1:
        print('Composite, Miller-Rabin witness '+ str(x) + '\n')
        exit()
    elif pow(x, d, n) in [1, phin]:
        continue
    else:
        for k in range(1,s):
            res = pow(x, d*pow(2,k), n)
            if res == 1:
                print('Composite, Miller-Rabin witness ' + str(x) + '\n')
                exit()
            elif res == phin:
                break
            else:
                pass


print('Probable prime')
