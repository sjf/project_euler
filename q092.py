#!/usr/bin/env python3
import lib
N=10_000_000



_memo={}
def chain(n):
  num = n
  while n not in [1,89]:
    if n in _memo:
      return _memo[n]
    nx = 0
    while n:
      nx += (n%10)**2
      n = n //10
    n = nx
  _memo[num] = n
  return n

count = 0
for i in range(1,N):
  if chain(i) == 89:
    count += 1
print(count)