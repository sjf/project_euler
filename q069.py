#!/usr/bin/env python3
import lib

N=1_000_000
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

def phi(n,mx):
  if sieve[n]:
    return n -1 # all numbers less than n are coprime

  result = 1 # 1 is coprime to all n

  fn = _factors[n]
  for i in range(n-1,1,-1):
    ff = _factors[i]
    #print(n,fn,i,ff,len(fn.intersection(ff)))
    coprime = 1
    for a in ff:
      if a in fn:
        coprime = 0
    result += coprime
    # if len(fn.intersection(ff)) == 0:
    #   result += 1

    rest = n-1-i
    if rest:
      mx_ratio = n/result + n/rest
      if mx_ratio < mx:
        #print('giving up', n, ' at ', i)
        result = n
        break

  return result

mx=0
mx_n=0
for n in range(2,N+1,2):
  ph = phi(n,mx)
  ratio = n/ph
  #print(' ',n,ph, ratio)
  if n % 1000 == 0: print(mx,mx_n,' ', n,ph, ratio)
  if ratio > mx:
    mx = ratio
    mx_n = n

print(mx,mx_n)