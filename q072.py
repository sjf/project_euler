#!/usr/bin/env python3
import lib, math
from collections import Counter
N=1_000_000

prime = lib.prime_sieve(N+1)

count = 0
for d in range(2,N+1):
  if prime[d]:
    count += d - 1
  else:
    count += lib.phi(d)
  if d % 10000 == 0:
    print('1/'+str(d),count)
print(count)
