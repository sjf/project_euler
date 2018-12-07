#!/usr/bin/env python3
import lib
count = 0
for pw in range(1,100):
  i = 1
  ln = 0
  while ln < pw+1:
    ln = lib.num_digits(i**pw)
    if ln == pw:
      print(i,'^',pw,i**pw)
      count += 1
    i += 1
print(count)