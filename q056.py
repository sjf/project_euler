#!/usr/bin/env python3
import lib
N=100

mx = 0
for i in range(1,100):
  for j in range(1,100):
    sm = sum(lib.to_digits(i**j))
    mx = max(sm,mx)

print(mx)