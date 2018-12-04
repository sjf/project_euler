#!/usr/bin/env python3
import math
N=100

uniq = {}
for a in range(2,N+1):
  for b in range(2,N+1):
    uniq[a**b] = 1
print(len(uniq))