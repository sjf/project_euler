#!/usr/bin/env python3

i = 1
s=""
while len(s) < 1_000_000:
  s += str(i)
  i += 1
result = 1
for i in range(7):
  result *= int(s[(10**i)-1])
print(result)