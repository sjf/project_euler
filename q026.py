#!/usr/bin/env python3
d=1000

mx = 3
mx_i = 0
for i in range(d-1, 1, -1):
  if mx > i:
    # max length of cycle is i
    continue

  frac = []
  n = 10
  if i > 99:
    n = 1000
    frac = [0,0]
  elif i > 9:
    n = 100
    frac = [0]
  cnt = 0

  while cnt < 2*i: # period will be length < i
    digit = int(n / i)
    frac.append(digit)
    if n % i == 0:
      break
    n = (n %i) * 10
    cnt += 1

    m = int(len(frac)/2)
    if m > mx and frac[:m] == frac[m:]:
      mx_i = i
      mx = m
      break
print(mx_i)

