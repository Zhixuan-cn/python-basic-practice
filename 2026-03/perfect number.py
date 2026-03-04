#A number is called a "perfect number" if it is exactly equal to the sum of its proper divisors. Find all perfect numbers within 1000.
for j in range(2, 1001):
    k = []
    s = j
    for i in range(1, int(j**0.5) + 1):
        if j % i == 0:
            if i != j:
                s -= i
                k.append(i)
            other = j // i
            if other != i and other != j:
                s -= other
                k.append(other)
    k.sort()
    if s == 0:
        print(j)
        print(' '.join(map(str, k)))
