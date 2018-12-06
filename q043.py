#!/usr/bin/env python3
import lib

def digits(d):
  if d == 0: return [0]
  result = []
  while d:
    result.append(d % 10)
    d = int(d/10)
  result.reverse()
  return result
def nodups(l):
  return len(set(l)) == len(l)
def removeNone(l):
  while None in l:
    l.remove(None)
def toNum(l):
  n = 0
  for i in l:
    n *= 10
    n += i
  return n

def get_overlapping(dA,dB):
  changed = False
  for i in range(len(dA)):
    d1 = dA[i]
    match = False
    for d2 in dB:
      if d1[1] == d2[0] and d1[2] == d2[1]:
        match = True
    if not match:
      dA[i] = None
      changed = True
  removeNone(dA)

  for i in range(len(dB)):
    d1 = dB[i]
    match = False
    for d2 in dA:
      if d1[0] == d2[1] and d1[1] == d2[2]:
        match = True
    if not match:
      dB[i] = None
      changed = True
  removeNone(dB)

  return changed

def get_candidates(n, filtr):
  i = 0
  result = []
  while lib.num_digits(i) < 4:
    i += n
    d = digits(i)
    if len(d) == 2:
      d.insert(0,0)
    if len(d) == 3 and nodups(d) and filtr(d):
      result.append(d)
  return result

d234 = get_candidates(2, lambda d:d[2] in [0,2,4,6,8])
d345 = get_candidates(3, lambda d:d[1] in [0,2,4,6,8])
d456 = get_candidates(5, lambda d:d[0] in [0,2,4,6,8] and d[2] in [0,5])
d567 = get_candidates(7, lambda d:d[1] in [0,5])
d678 = get_candidates(11, lambda d:d[0] in [0,5])
d789 = get_candidates(13, lambda d:True)
d8910 = get_candidates(17, lambda d:True)

parts = [d234, d345, d456, d567, d678, d789, d8910]

changed = True
while changed:
  changed = False
  for i in range(len(parts)-1):
    changed |= get_overlapping(parts[i],parts[i+1])

def getnums(parts, partial):
  if not parts:
    return [partial]
  result = []
  for d in parts[0]:
    if partial[-2] == d[0] and partial[-1] == d[1] and d[2] not in partial:
      nextp = partial[:]
      nextp.append(d[2])
      result.extend(getnums(parts[1:], nextp))
  return result

suffixes = []
for part in parts[0]:
  suffixes.extend(getnums(parts[1:], part))

sum = 0
for n in suffixes:
  for i in range(0,10):
    if i not in n:
      d = n[:]
      d.insert(0, i)
      sum += toNum(d)

print(sum)
