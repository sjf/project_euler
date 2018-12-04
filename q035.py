#!/usr/bin/env python3
import lib
N=1_000_000

sieve = lib.get_prime_sieve(N)
primes = lib.primes(N, sieve)

def rotate(n):
  cnt = n_digits(n)
  result = [n]
  for i in range(cnt-1):
    d = n % 10
    n = int(n /10)
    n += d * 10**(cnt-1)
    result.append(n)
  return result

def n_digits(n):
  if n == 0:
    return 1
  c = 0
  while n:
    n = int(n/10)
    c += 1
  return c

cnt = 0
for i in primes:
  is_circular = True
  for n in rotate(i):
    if not sieve[n]:
      is_circular = False
  if is_circular:
    cnt += 1

print(cnt)