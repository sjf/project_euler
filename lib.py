# -*- coding: utf-8 -*-

from functools import reduce
from collections import Counter

def prime_factors(n):
  """ Returns the prime factors of n."""
  assert isinstance(n, int)

  result = []
  p=2
  while p**2 <= n:
    if n % p == 0:
      result.append(p)
      n /= p
    else:
      p += 1
  result.append(int(n))
  return result

def get_factors(n):
  """ Returns the factors of n."""
  assert isinstance(n, int)
  if n == 1: return [1]
  # Get the prime factors of n, in the form p1^a, p2^b, p3^c
  prime_facs = Counter(prime_factors(n))
  # The factors of n are formed from every combination of the prime exponents
  return _get_factors(list(prime_facs.items()))

def _get_factors(pairs, partial=1):
  """ Return all factors from pairs of the prime factors and their exponents."""
  if not pairs:
    return [partial]
  result = []
  (num, exp) = pairs[0]
  for i in range(exp+1):
    result.extend(_get_factors(pairs[1:], partial * num**i))
  return result

def primes(n, sieve = None):
  """ Returns the prime numbers up to n."""
  assert isinstance(n, int)
  assert sieve is None or len(sieve) == n 

  if not sieve:
    sieve = get_prime_sieve(n)
  result = []
  for i in range(2, n):
    if sieve[i]:
      result.append(i)
  return result

def get_prime_sieve(n):
  assert isinstance(n, int)
  # Sieve of Eratosthenes
  sieve = [True for i in range(0, n)]
  sieve[0] = sieve[1] = False # 1 is not prime
  for i in range(2, n):
    if sieve[i]:
      mul = 2
      while mul*i < n:
        sieve[mul*i] = False
        mul += 1
  return sieve

def is_prime(n):
  assert isinstance(n, int)
  if n < 0: n = -n

  # look for prime divisors of n
  # all primes > 3 are of the form 6k±1
  if n <= 3:
   return True
  if n % 2 == 0 or n % 3 == 0:
   return False
  i = 6
  while i < n-1:
    if n % (i + 1) == 0:
      return False
    if n % (i - 1) == 0:
      return False
    i += 6  
  return True

def num_digits(n):
  if n == 0:
    return 1
  c = 0
  while n:
    n = int(n/10)
    c += 1
  return c

def is_pandigital(n):
  if n == 0:
    return False
  # for each digit d of n, the binary digit in position d will be
  # set to 1.
  accum = 0
  # target will have binary digit set to 1 in each position
  # 1-number of digits in n
  target = 0
  while n:
    d = n %10
    n = int(n/10)
    accum |= 1 << d
    target = (target << 1) | 1
  target = target << 1 # right shift one for zero digit position

  return accum == target

def multiply(l):
  assert isinstance(l, list)
  return reduce(lambda x, y: x*y, l)
def first(p):
  return p[0]
def second(p):
  return p[1]
def push(l, item):
  l.insert(0, item)
  return l
def print2d(l):
  print(",\n".join(map(str, l)))
