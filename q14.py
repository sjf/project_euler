#!/usr/bin/env python3

N=1_000_000

_memo = {}
def collatz(n):
  ln = _collatz(n)
  _memo[n] = ln
  return ln

def _collatz(n):
  ln = 1
  while n != 1:
    if n % 2 == 0:
      n = int(n/2)
    else:
      n = 3 * n + 1
    ln += 1
    if n in _memo:
      return ln + _memo[n]
  return ln

i = 2
max_len = 0
max_n = 0
while i < N:
  ln = collatz(i)
  if ln > max_len:
    max_len = ln
    max_n = i
  i += 1
print(max_n)
