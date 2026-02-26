# Calculate how many prime numbers are between 101 and 200, and output all prime numbers.
p = 0
is_prime = 1
from math import sqrt
for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            is_prime = 0
            break
    if is_prime == 1:
        print(f"{m:<4}")
        p += 1
    is_prime = 1
print(f"The total is {p}")
