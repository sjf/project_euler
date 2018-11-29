#!/usr/bin/env python3
import sys

def is_palindrome(n):
  return n == reverse(n)

def reverse(n):
  assert isinstance(n, int)
  res = 0
  while n:
    res *= 10
    res += n % 10
    n = int(n / 10)
  return res

def get_factors(n):
  a = 100
  while a < 1000:
    if n % a == 0:
      b = n / a
      if 100 <= b < 1000:
        return (a, int(n/a))
    a += 1
  return None

N=999*999
while N > 99999:
  if is_palindrome(N):
    factors = get_factors(N)
    if factors:
      print(N)
      sys.exit(0)
  N -= 1