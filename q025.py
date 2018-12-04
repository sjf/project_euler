#!/usr/bin/env python3
f=1
fprev=1
n=2
while f < 10**999:
  f,fprev = f + fprev,f
  n += 1

print(n)