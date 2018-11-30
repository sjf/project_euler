from functools import reduce
from collections import Counter

def prime_factors(n):
  """ Returns the prime factors of n."""
  assert isinstance(n, int)

  result = []
  p=2
  while n >= p**2:
    if n % p == 0:
      result.append(p)
      n /= p
    else:
      p += 1
  result.append(int(n))
  return result

def primes(n):
  """ Returns the prime numbers up to n."""
  assert isinstance(n, int)

  composite = [False for i in range(0, n)]
  for i in range(2, n):
    if not composite[i]:
      mul = 2
      while mul*i < n:
        composite[mul*i] = True
        mul += 1
  result = []
  for i in range(2, len(composite)):
    if not composite[i]:
      result.append(i)
  return result

def multiply(l):
  assert isinstance(l, list)
  return reduce(lambda x, y: x*y, l)

def get_factors(n):
  """ Returns the factors of n."""
  assert isinstance(n, int)
  prime_facs = Counter(prime_factors(n))
  return _get_factors(list(prime_facs.items()))

def _get_factors(pairs, partial=1):
  """ Return all factors from the prime factors."""
  if not pairs:
    return [partial]
  result = []
  (num, exp) = pairs[0]
  for i in range(exp+1):
    result.extend(_get_factors(pairs[1:], partial * num**i))
  return result


