#!/usr/bin/env python3

S=open('p067_triangle.txt').read().strip()

t = list(map(lambda line: list(map(int, line.split(' '))), S.split('\n')))

for i in range(1, len(t)):
  t[i][0] += t[i-1][0]
  n = len(t[i])-1
  t[i][n] += t[i-1][n-1]

  for j in range(1, len(t[i])-1):
    t1 = max(t[i-1][j-1],t[i-1][j])
    t[i][j] += t1

print(max(t[-1]))
