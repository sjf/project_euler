#!/usr/bin/env python3
from math import factorial
N=100
def n_choose_r(n, r):
  return int(factorial(n)/(factorial(r)*factorial(n-r)))
count = 0
n=N
while n:
  r = 1
  while r <= n:
    res = n_choose_r(n,r)
    if res > 1_000_000:
      count += 1
    r += 1
  n -=1
print(count)