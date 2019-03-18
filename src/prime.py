import sys
import math



def isPrime(x):
    # sieve of erastosthenes
    primes = []
    nonprimes = []
    for i in range(2, x + 1):
        # if i is not in the list of nonprimes
        # print(f'i is {i}')
        if nonprimes.count(i) == 0:
            primes.append(i)
            # print('primes:', primes)
            j = i + i
            while j < x + 1:
                # print(f'j is {j}')
                if j == x:
                    return False
                else:
                    nonprimes.append(j)
                    j = j + i
    # print('primes:', primes)
    # print('nonprimes:', nonprimes)
    return True


if len(sys.argv) != 2:
    print('usage: ./prime [num]')
    sys.exit()

try:
    num = int(sys.argv[1])
    print(f'{num} is prime') if isPrime(num) else print(f'{num} is not prime')
# catch if string is passed as argument
except ValueError:
    print('Please pass a valid number as an argument')
