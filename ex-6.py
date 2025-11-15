#Find all pseudoprimes to the base 2. That is, find composite integers n such that 2^(n−1)≡1(mod n), where n does not exceed 10000.
def is_prime(n):
    """check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_pseudoprimes(limit):
    """Find all composite numbers n <= limit where 2^(n-1) ≡ 1 (mod n)"""
    pseudoprimes = []
    
    for n in range(2, limit + 1):
        # Skip prime numbers (we only want composites)
        if is_prime(n):
            continue
            
        # Check if 2^(n-1) ≡ 1 (mod n)
        # Using pow with modulus for efficiency
        if pow(2, n-1, n) == 1:
            pseudoprimes.append(n)
    
    return pseudoprimes

# Find pseudoprimes up to 10000
limit = 10000
pseudoprimes = find_pseudoprimes(limit)

print(f"Fermat pseudoprimes to base 2 (n ≤ {limit}):")
print(f"Total found: {len(pseudoprimes)}")
print("\nList of pseudoprimes:")
for i, p in enumerate(pseudoprimes, 1):
    print(f"{p}", end=", " if i % 8 != 0 else "\n")

print(f"\n\nFirst few with their prime factorizations:")
# Show factorizations for first 10
for p in pseudoprimes[:10]:
    factors = []
    temp = p
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    print(f"{p} = {' × '.join(map(str, factors))}")