#!/usr/bin/env python3
import lib
N=28124 # all numbers below this are sum of 2 abundant numbers
LOW=12 # lowest abundant number
abundant = []

for i in range(LOW, N):
  factors = lib.get_factors(i)
  factors.remove(i)
  sm = sum(factors)
  if sm > i:
    abundant.append(i)

is_sum = {}
for i in range(len(abundant)):
  for j in range(i, len(abundant)):
    n = abundant[i] + abundant[j]
    is_sum[n] = n
result = 0
for i in range(N):
  if i not in is_sum:
    result += i
print(result)
 

