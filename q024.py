#!/usr/bin/env python3
from math import factorial
N=1_000_000
D=list(range(0,10))

def f(digits, nth):
  if not digits:
    return ""
  rest  = factorial(len(digits) - 1)
  d = int(nth / rest)
  res = digits[d]
  digits.remove(res)
  return str(res) + f(digits, nth % rest)

print(f(D, N-1))