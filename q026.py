#!/usr/bin/env python3
d=1000

for i in range(2,d):
  n = 10
  frac = []
  cnt = 0
  while cnt < 100:
    digit = int(n / i)
    if digit in frac:
      print(i, "1."+"".join(map(str,frac)))
      break
    frac.append(digit)
    if n % i == 0:
      break
    n = (n %i) * 10
    cnt += 1
  #print(i, frac)

