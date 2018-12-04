#!/usr/bin/env python3
import lib
N=1000000

sieve = lib.get_prime_sieve(N)
primes = lib.primes(N, sieve)
primes = primes[4:]

def is_truncatable(n):
  num = n
  c = 0
  while num:
    if not sieve[num]:
      return False
    num = int(num / 10)
    c += 1

  while c:
    num = n % 10**c
    if not sieve[num]:
      return False
    c -= 1
  return True
    
result = []
for i in primes:
  if is_truncatable(i):
    result.append(i)
    if len(result) == 11:
      break
    
print(sum(result))