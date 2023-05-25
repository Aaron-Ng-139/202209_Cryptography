# Miller-Rabin Test
# We are finding a 14-bit integer meaning num < 16384 (2^14)
# We want confidence of t = 5

import random

# Find k,q with k > 0, odd(q), n-1 = 2^k * q
def find_k_q(n) :
    n = n - 1
    if n % 2 == 1:
        return False
    k = 0
    while n % 2 == 0:
        n = n // 2
        k = k + 1
    if n % 2 == 1:
        q = n
        return [k, q]
    else:
        return False

# Miller-Rabin Algorithm
def MillerRabin(n):
    
    # Base cases
    if n < 2:
        return "composite"
    elif n == 2 or n == 3:
        return "prime"

    # Find k, q
    k_q = find_k_q(n)
    if k_q is False:
        print("Unable to represent " + str(n) + " as 2^k * q")
        return "composite"
    else:
        k = k_q[0]
        q = k_q[1]

    # Select random integer a
    a = random.randrange(2, n - 1)
    print(str(a) + " selected as random int a")

    if (a**q) % n == 1:
        return "inconclusive"
    
    for j in range(k): # From 0 to k-1
        if (a**((2**j) * q)) % n == n-1:
            return "inconclusive"
    
    return "composite"


# Change this number to what you want to test
TEST_NUM = 10243 # I got this number from various tries on random.org
inc = 0

for i in range(5):
    result = MillerRabin(TEST_NUM)
    if result == "composite":
        print("Number is composite")
        break
    elif result == "prime":
        print("Number is prime")
        break
    elif result == "inconclusive":
        inc = inc + 1
    else:
        print("error")

if inc >= 5:
    print(str(TEST_NUM) + " is probably prime w/ confidence of t=5")

# It so happens that 10243 is on the list of primes on 
# https://primes.utm.edu/lists/small/10000.txt