#!/usr/bin/env python3
import lib

def to_binary(n):
  if n == 0:
    return 0
  num = ''
  while n:
    num = str(n % 2) + num
    n = int(n/2)
  return num

def is_palindrome(s):
  n = len(s)
  for i in range(int(n/2)):
    if s[i] != s[n-i-1]:
      return False
  return True

sum = 0
for i in range(1, 10):
  if (is_palindrome(to_binary(i))):
    sum += i

# All even length base 10 palindromes
for i in range(1, 1000):
  num = i
  while i:
    num *= 10
    num += i % 10
    i = int(i/10)
  if (is_palindrome(to_binary(num))):
    sum += num

# All odd length base 10 palindromes
for i in range(1, 100):
  num = i
  num *= 10
  c = 0
  while i:
    num *= 10
    num += i % 10
    i = int(i/10)
    c += 1
  for j in range(0,10):
    n = num +  j * 10**(c)
    if (is_palindrome(to_binary(n))):
      sum += n
print(sum)