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

def eval_continued_fraction(terms):
  if not terms:
    return 0,1
  if len(terms) == 1:
    return terms[0],1

  d = terms.pop()
  n = 1
  while len(terms) > 1:
    n = terms.pop()*d + n
    n,d = d,n
  # First entry in terms is a whole number
  n += d*terms.pop()
  return n,d

count = 0
for i in range(1,N+1):
  n,d = eval_continued_fraction(get_e_continued_fraction(i))
  print(i, lib.fraction_tostr(n,d))

n,d = eval_continued_fraction(get_e_continued_fraction(100))
print(sum(lib.to_digits(n)))
