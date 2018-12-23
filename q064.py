#!/usr/bin/env python3
from math import sqrt
N=10_000

def get_sqrt_fraction(n):
  # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
  m = 0
  d = 1
  a = a0 = int(sqrt(n))

  result = []
  result.append(a)
  if a**2 == n: 
    # n does not have an irrational sq root
    return result

  while a != 2*a0: # period ends when a == 2*a0
    m = d*a - m
    d = (n - m**2)/d
    a = int((a0 + m)/d)
    result.append(a)
  return result


count = 0
for i in range(1,N+1):
  fraction = get_sqrt_fraction(i)
  print(i, fraction)
  if len(fraction[1:]) %2 == 1:
    count += 1

print(count)