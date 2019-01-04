#!/usr/bin/env python3
import lib, math
from collections import Counter
N=12_000

prime = lib.prime_sieve(N+1)

count = 0
for d in range(2,N+1):
  for n in range(int(d/3), int(d/2)+1):
    if 2*n >= d: #n/d >= 1/2
      break
    if 3*n > d: #n/d > 1/3
      if prime[d]:
        count += 1
      elif lib.gcd(n,d) == 1:
        count += 1
  if d % 100 == 0:
    print('d = '+str(d), count)
print(count)
