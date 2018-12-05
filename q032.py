#!/usr/bin/env python3
import lib

def eligible(a,b,c):
  digits = {}
  if has_dups(a, digits):
    return False
  if has_dups(b, digits):
    return False
  if has_dups(c, digits):
    return False
  if 0 in digits:
    return False
  for i in range(1,10):
    if i not in digits:
      return False
  return True

def has_dups(n, digits=None):
  if n == 0:
    return True
  if digits is None:
    digits = {}
  while n:
    d = n%10
    n = int(n/10)
    if d in digits:
      return True
    digits[d] = 1
  return False

products = {}
for i in range(1, 100): # 1-2 digits
  if not has_dups(i):
    if i < 10:
      rng = range(1000, 100_000) # 3-5 digits
    else:
      rng = range(100, 1000) # 2-3 digits
    for j in rng: 
      p = i * j
      if eligible(i,j,p):
         print(p,i,j)
         products[p] = 1
      if lib.num_digits(p) + lib.num_digits(i) + lib.num_digits(j) > 9:
        break

print(sum(products.keys()))

