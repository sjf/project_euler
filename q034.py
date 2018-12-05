#!/usr/bin/env python3
from math import factorial
N=10000000

def facsum(n):
  if n == 0:
    return 1
  sm = 0
  while n:
    sm +=factorial(n % 10)
    n = int(n/10)
  return sm

sm = 0
for i in range(3, N):
  if i == facsum(i):
    sm += i
print(sm)