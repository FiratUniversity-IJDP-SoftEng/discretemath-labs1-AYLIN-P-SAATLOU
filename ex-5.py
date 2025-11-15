#Find 10 different prime numbers, each with 100 digits. (This task may require online research or special libraries.)
#!pip install sympy
from sympy import randprime, isprime

def find_large_primes():
    print("Finding 10 different 100-digit prime numbers...\n")
    
    # Define the range for 100-digit numbers
    lower_bound = 10**99    # smallest 100-digit number (1 followed by 99 zeros)
    upper_bound = 10**100 - 1  # largest 100-digit number (99 nines)
    
    primes = []
    attempts = 0
    max_attempts = 50
    
    while len(primes) < 10 and attempts < max_attempts:
        attempts += 1
        try:
            # Generate a random prime in our range
            prime = randprime(lower_bound, upper_bound)
            if prime not in primes:  # Ensure uniqueness
                primes.append(prime)
                print(f"Prime #{len(primes)}: {prime}")
        except ValueError:
            # If no prime found in range, try again
            continue
    
    return primes

# This will take some time to run
primes = find_large_primes()
print(f"\nFound {len(primes)} unique 100-digit primes")
