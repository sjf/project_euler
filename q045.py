#!/usr/bin/env python3
import lib
N=1000000

for n in range(40755,N):
  t = lib.triangle(n)
  if lib.is_pentagonal(t) and lib.is_hexagonal(t):
    print(t)
