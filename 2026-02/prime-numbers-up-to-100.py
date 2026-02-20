import math

def is_prime(n):
    """
    Determine if a number is a prime number
    :param n: 
    :return: True（prime）/ False（non prime）
    """
    # Numbers less than 2 are not prime numbers
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Even numbers greater than 2 are not prime numbers
    if n % 2 == 0:
        return False
    # Check the odd numbers from 3 to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_up_to_100():
    """Find all prime numbers within 100 and output them"""
    primes = []
    # Iterate through all numbers from 2 to 100
    for num in range(2, 101):
        if is_prime(num):
            primes.append(num)
    # output
    print("What are the prime numbers within 100?：")
    # Display 10 per line
    for i, prime in enumerate(primes):
        print(prime, end="\t")
        if (i + 1) % 10 == 0:  
            print()
    print(f"\n\nthere are {len(primes)} primes within 100")

# Execute function
if __name__ == "__main__":
    find_primes_up_to_100()
