#!/usr/bin/env python3
import re
from collections import Counter

def fix(s):
  # Replace 9 VIIII with IX
  s = re.sub('VIIII$','IX', s)
  # Replace 4 IIII with IV
  s = re.sub('IIII$','IV', s)
  # Replace 90 LXXXX with XC
  s = re.sub('LXXXX','XC', s)
  # Replace 40 XXXX with XL
  s = re.sub('XXXX','XL', s)
  # Replace 900 DCCCC with CM
  s = re.sub('DCCCC','CM', s)
  # Replace 400 CCCC with CD
  s = re.sub('CCCC','CD', s)
  return s

def assertone(c, s):
   cnt = Counter(s)
   if c in cnt:
    assert cnt[c] == 1

def ok(s):
  for c in "DLV":
    assertone(s, c)
  return s



lines = open('p089_roman.txt').read().strip().split('\n')

count = 0
for line in lines:
  nline = ok(fix(line))
  count += len(line) - len(nline)
  if line != nline:
    print(line, nline)
print(count)