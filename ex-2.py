#Write a function that lists all prime numbers less than or equal to a given positive integer.
def list_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)
    return primes

num = int(input("Enter a positive integer: "))
print("Prime numbers up to", num, ":", list_primes(num))
