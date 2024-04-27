def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]

# решением является эта функция
def prime_numbers_in_range(min_num, max_num):
    primes = sieve_of_eratosthenes(max_num)
    return [num for num in primes if num >= min_num]

