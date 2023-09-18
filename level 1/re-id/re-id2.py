def get_divisors(n):
    divisors = []
    for i in xrange(1, (n/2)+1):
        if n%i == 0:
            divisors.append(i)
    return divisors

def is_prime(n):
    return len(get_divisors(n)) == 1

def concatenate_primes(length):
    primes = ''
    current_num = 2
    adder = 1
    while len(primes) <= length + 4:
        if is_prime(current_num):
            primes = primes + str(current_num)
        current_num += adder
        if current_num == 3:
            adder = 2
    return primes

def solution(n):    
    prime_string = concatenate_primes(n)
    return ''.join(prime_string[n:n + 5])