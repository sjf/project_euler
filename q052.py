#!/usr/bin/env python3
import lib
N=1000000

i = 1
for i in range(1,N):
  target = lib.to_digits(i)
  target.sort()
  ok = True
  for j in range(2,6):
    m = lib.to_digits(i*j)
    m.sort()
    ok &= m == target
  if ok:
    print(i)
    break
