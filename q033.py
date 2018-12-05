#!/usr/bin/env python3

result_n = 1
result_d = 1

for denom in range(11,100):
  for numer in range(10,denom):
    d1 = numer%10
    d2 = int(numer/10)
    d3 = denom%10
    d4 = int(denom/10)

    candidates = {}
    if d1 == d3 and d1 != 0:
      candidates[(d2,d4)] = 1
    if d1 == d4 and d1 != 0:
      candidates[(d2,d3)] = 1
    if d2 == d3 and d2 != 0:
      candidates[(d1,d4)] = 1
    if d2 == d4 and d2 != 0:
      candidates[(d1,d3)] = 1

    for n,d in candidates:
      if n != 0 and d != 0:
        if float(n)/d == float(numer)/denom:
          print(numer,'/',denom,' ',n,'/',d)
          result_n *= n
          result_d *= d

print(result_n,'/',result_d)

