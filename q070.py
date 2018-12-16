#!/usr/bin/env python3
import lib

N=10_000_000
sieve = lib.prime_sieve(N+1)
_factors = {}

def prime_factors(n):
  if n in _factors:
    return _factors[n]
  if sieve[n]:
    _factors[n] = [n]
    return set([n])

  num = n
  result = set()
  p=2
  while p**2 <= n:
    if n % p == 0:
      result.add(p)
      n //= p
    else:
      p += 1
    if n in _factors:
      result.update(_factors[n])
      _factors[num] = result
      return result
      
  result.add(int(n))
  _factors[n] = result
  return result

for i in range(N+1):
  _factors[i] = prime_factors(i)
  #if not i % 10000: print(i)
print('.')

def factors(n):
  if sieve[n]:
    return [n]
  if n in _factors:
    return _factors[n]
  raise Exception("n out of range")

def phi(n):
  if sieve[n]:
    return n-1 # all numbers less than n are coprime

  fn = _factors[n]
  result = n
  for f in fn:
    result *= (1 - 1/f)
  return result

def ok(n,ph):
  ndigits = lib.to_digits(n)
  phdigits = lib.to_digits(ph)
  if len(ndigits) != len(phdigits):
    return False
  ndigits.sort()
  phdigits.sort()
  return ndigits == phdigits

mn=None
mn_n=0
for n in range(2,N+1):
  ph = phi(n)
  ratio = n/ph
  #print(' ',n,ph, ratio)
  # if n % 1000 == 0: print(n,ph,mn,mn_n,' ', ratio)
  if ok(n,ph):
    print('**',n,ph, ratio)
    if not mn or ratio < mn:
      mn = ratio
      mn_n = (n,ph)

print(mn,mn_n)