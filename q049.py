#!/usr/bin/env python3
import lib
N=10000
from collections import defaultdict
sieve = lib.get_prime_sieve(N)

_memo = {}
def check(i):
  if not sieve[i]: 
    return
  if i in _memo:
    return
  perms = set(map(lib.to_num, lib.permutations(lib.to_digits(i))))

  pperms = []
  for perm in perms:
    if sieve[perm] and perm >= 1000:
      pperms.append(perm)
    _memo[perm] = True

  if len(pperms) < 3: 
    return
  pperms.sort()

  for i in range(len(pperms)):
    for j in range(i+1,len(pperms)):
      a,b = pperms[i],pperms[j]
      diff = b-a
      c = b + diff
      if c in pperms:
        print("".join(map(str,[a,b,c])))
        
for i in range(1000,N):
  check(i)
