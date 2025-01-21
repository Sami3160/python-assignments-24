def sieve_of_eratosthenes(limit):
    # Initialize a boolean list to track prime numbers
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    # Mark all non-prime numbers
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    return sieve

def sum_of_primes(limit):
    # Get the list of primes using sieve
    sieve = sieve_of_eratosthenes(limit)
    
    # Sum the primes
    return sum(i for i in range(limit) if sieve[i])

# Set the limit to two million
limit = 2000000
result = sum_of_primes(limit)
print(f"The sum of all primes below {limit} is: {result}")