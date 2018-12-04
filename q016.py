#!/usr/bin/env python

N=1000
digits = [1]
for i in range(1, N + 1):

  digits=list(map(lambda x:x*2,digits))
  for j in range(len(digits)-1):
    if digits[j] >= 10:
      digits[j] %= 10
      digits[j+1] += 1
  j = len(digits)-1
  if digits[j] >= 10:
    digits.append(1)
    digits[j] %= 10


print(sum(digits))