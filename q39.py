#!/usr/bin/env python3

N=1000
max_solutions=0
result = 0
for p in range(1, N):
  solutions = 0
  for a in range(1, int(p/3)):
    # formula for b: b=(p^2 - 2ap)/(2p-2a)
    # from a^2 + b^2 = c^2 and p = a + b + c
    # if b is integer, a&b are pythagorean triple
    if p*(p-2*a) % (2*p - 2*a) == 0:
      solutions += 1
  if solutions >= max_solutions:
    result = p
    max_solutions = solutions

print(result)
