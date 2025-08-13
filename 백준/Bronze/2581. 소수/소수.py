def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

prime_sum = 0
min_prime = None

for number in range(M, N + 1):
    if is_prime(number):
        prime_sum += number
        if min_prime is None:
            min_prime = number

if min_prime is not None:
    print(prime_sum)
    print(min_prime)
else:
    print(-1)