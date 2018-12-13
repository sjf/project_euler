#!/usr/bin/env python3
import lib
from collections import defaultdict
MN=1
N=100000

def key(n):
  l = lib.to_digits(n)
  l.sort()
  i = 0
  while l[0] == 0:
    l.pop(0)
    l.append(0)
  return lib.to_num(l)

d=defaultdict(list)

i = MN
while i < N:
  n = i**3
  k = key(n)
  d[k].append(n)
  if len(d[k]) == 5:
    print(i,d[k],len(d[k]))
    i = N
  i += 1

