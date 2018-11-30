from functools import reduce

def prime_factors(n):
  """ Returns the prime factors of n."""
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

