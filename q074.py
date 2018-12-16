#!/usr/bin/env python3
import lib
from math import factorial

N=1_000_000

# n -> length chain before repeat
_memo = {}

def fact_sum(n):
  result = 0
  while n:
    result += factorial(n%10)
    n//=10
  return result

def chain(num):
  previous = {}
  count = 0
  n = num
  while n not in previous:
    previous[n] = True
    n = fact_sum(n)
    count += 1
    if n in _memo:
      count += _memo[n]
      break

  _memo[num] = count
  return count

result = 0
for n in range(1,N):
  ln = chain(n)
  #print(n,ln)
  if ln == 60:
    print(n,ln)
    result += 1
print(result)
