#!/usr/bin/env python3
import lib
from collections import defaultdict

L=1_500_000

def odd(n):
  return n % 2 == 1

triangles = defaultdict(set)

for n in range(1, int((L//2)**0.5)):
  n2 = n**2
  for m in range(n+1, int((L//2)**0.5)): # n must be less than m
    if not(odd(m) and odd(n)) == 1 and lib.gcd(m,n) == 1: # conditions for a primitive pythagorean triple
      m2 = m**2
      k = 1
      # Euclid's formula for pythagorean triples
      a,b,c = m2 - n2, 2*m*n, m2 + n2
      l = a+b+c
      if l > L:
        break
      while a+b+c <= L:
        l = [a,b,c]
        l.sort()
        triangles[a+b+c].add(tuple(l))
        k += 1
        a,b,c = (m2 - n2)*k, 2*m*n*k, (m2 + n2)*k

count = 0
for k,v in triangles.items():  
  if len(v) == 1:
    count += 1
print(count)




