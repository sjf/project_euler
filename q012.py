#!/usr/bin/env python3
import sys,lib
N=500

i = 1
while 1:
  t = int((i**2 + i)/2)
  n_factors = len(lib.get_factors(t))
  if n_factors > N:
    print(t)
    sys.exit(0)
  i += 1
