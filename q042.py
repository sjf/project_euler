#!/usr/bin/env python3
import lib

sums = lib.sum_words(lib.read_words_from_file('p042_words.txt'))
mx = max(sums)

triangle = {}
t = 0
i = 1
while t < mx:
  t = int(i*(i + 1)/2)
  triangle[t] = True
  i += 1

cnt = 0
for sm in sums:
  if sm in triangle:
    cnt += 1
print(cnt)