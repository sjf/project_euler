#!/usr/bin/env python3
import lib
N=10_000

d={}
for i in range(1,N):
  factors = lib.get_factors(i)
  factors.remove(i)
  d[i] = sum(factors)

result = 0
for i in range(2,N):
  val = d[i]
  if val < N and val != i and d[val] == i:
    result += i

print(result)