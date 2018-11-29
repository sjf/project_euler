from functools import reduce

def prime_factors(n):
  res = [1]
  p=2
  while n >= p**2:
    if n % p == 0:
      res.append(p)
      n /= p
    else:
      p += 1
  res.append(int(n))
  return res

def multiply(l):
  assert isinstance(l, list)
  return reduce(lambda x, y: x*y, l)