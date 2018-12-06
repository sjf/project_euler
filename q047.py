#!/usr/bin/env python3
import lib
from collections import Counter
N=1000000
D=4

for i in range(N):
  pfactors=set()
  ok = True
  j = 0
  while j < D and ok:
    f = Counter(lib.prime_factors(i+j))
    if len(f.keys()) != D:
      ok = False
    if ok: 
      pfactors.update(f.items())
    j += 1
  if ok and len(pfactors) == D*D:
    print(i)
    break
