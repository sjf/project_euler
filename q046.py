#!/usr/bin/env python3
import lib
from math import sqrt
N=1000000
sieve = lib.get_prime_sieve(N)
primes = lib.primes(N,sieve)

for i in range(9,N,2):
  if sieve[i]: continue #not composite
  ok = False
  for j in range(i-2,2,-1):
    if sieve[j]:
      diff = i-j
      if diff % 2 == 0 and lib.isint(sqrt(diff/2)):
        ok = True
        break
  if not ok:
    print(i)
    break

