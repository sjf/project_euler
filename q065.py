#!/usr/bin/env python3
import lib
N=10

def get_e_continued_fraction(n):
  """ Return the first n digits of the continued fraction of e."""
  if not n:
    return []
  result = [2] # First digit
  n -= 1
  k = 1
  # Pattern is 1,2k,1...
  for i in range(n):
    if i % 3 == 1:
      result.append(k * 2)
      k += 1
    else:
      result.append(1)
  return result



count = 0
for i in range(1,N+1):
  n,d = lib.eval_continued_fraction(get_e_continued_fraction(i))
  print(i, lib.fraction_tostr(n,d))

n,d = lib.eval_continued_fraction(get_e_continued_fraction(100))
print(sum(lib.to_digits(n)))
