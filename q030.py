#!/usr/bin/env python3
N=6*(9**5)
P=5
def sum_power_digits(n, pw):
  if n == 0:
    return 0  
  sum = 0
  while n:
    d = n % 10
    n = int(n / 10)
    sum += d**pw
  return sum

sum = 0
for i in range(2, N):
  if sum_power_digits(i, P) == i:
    sum += i
print(sum)