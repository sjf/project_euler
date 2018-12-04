#!/usr/bin/env python3

N=10000 # str(10000) + str(2*10000) => 10 digit number 

def ispandigital(s):
  for i in range(1,10):
    if str(i) not in s:
      return False
  if "0" in s:
    return False
  return True

def hasdups(s):
  l = list(s)
  l.sort()
  for i in range(0, len(l)-1):
    if l[i] == l[i+1]:
      return True
  return False

mx = ""
for i in range(2,N):
  j = 1
  concat = ""
  while not ispandigital(concat) and not hasdups(concat):
    concat += str(i * j)
    j+= 1
  if ispandigital(concat) and not hasdups(concat):
    if concat > mx:
      mx = concat
print(mx)
