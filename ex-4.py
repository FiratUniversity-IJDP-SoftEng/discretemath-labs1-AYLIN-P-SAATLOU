#Show (test with code) that n^2+n+41 is prime for all integers n with 0≤n≤39. But also show that it is not prime when n=40.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test n=0 to 39
print("Testing n=0 to 39:")
all_prime = True
for n in range(40):
    result = n*n + n + 41
    if not is_prime(result):
        all_prime = False
        print(f"n={n}: {result} is not prime!")
        break

if all_prime:
    print("All n=0 to 39 are prime ✓")

# Test n=40
print(f"\nTesting n=40:")
result = 40*40 + 40 + 41
print(f"40² + 40 + 41 = {result}")
print(f"Is prime? {is_prime(result)}")
print(f"Factors: 41 × 41 = {41*41}")
