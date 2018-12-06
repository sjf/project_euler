#!/usr/bin/env python3
import lib
N=7654321

for i in range(N,1234566,-2):
  if lib.is_pandigital(i):
    #print(i)
    factors = lib.get_factors(i)
    if len(factors) == 2:
      print(i)
      break

