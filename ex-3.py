#Use a loop and the function above to determine whether 2p−1 is prime for each prime number p not exceeding 100.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def list_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

primes_up_to_100 = list_primes(100)


for p in primes_up_to_100:
    m = 2**p - 1
    if is_prime(m):
        print(f"2^{p} - 1 = {m} is prime")
    else:
        print(f"2^{p} - 1 = {m} is not prime")
