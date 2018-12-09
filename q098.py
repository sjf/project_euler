#!/usr/bin/env python3
import lib
from collections import defaultdict
words = lib.read_words_from_file('p098_words.txt')

d=defaultdict(list)
for w in words:
  key = list(w)
  key.sort()
  d[tuple(key)].append(w)

pairs = []
mx = 0
for k in d:
  val = d[k]
  if len(val) > 1:
    pairs.append(val)

pairs =  sorted(pairs, key=lambda a:len(a[0]))
pairs.reverse()

MX = 10**9 # longest word has 9 chars
squares = defaultdict(list)
i = 1
while i**2 < MX:
  sq = i**2
  squares[lib.num_digits(sq)].append(sq)
  i += 1  

def assign(num,word):
  code = {}
  for c,d in zip(word,lib.to_digits(num)):
    if c in code and code[c] != d:
      return None
    if d in code.values():
      return None # d already mapped to a char
    code[c] = d
  return code

def to_num(code,word):
  result = 0
  for c in word:
    d = code[c]
    result *= 10
    result += d
  if len(word) != lib.num_digits(result): # leading digits cannot be 0
    return 0 
  return result

def is_sq(n):
  rt = n**0.5
  return lib.isint(rt)

def find_sq(words):
  mx = 0
  a = words[0]
  candidates = squares[len(a)]
  for num in candidates:
    code = assign(num,a)
    if not code:
      continue
    nums = []
    for word in words:
      num = to_num(code,word)
      if num and is_sq(num):
        #print(word,num)
        nums.append(num)
      else:
        break
    if len(nums) == len(words): # all words mapped to squares
      print(nums,words)
      mx=max(mx,max(nums))
  return mx

#pairs=[['CARE','RACE']]
result = 0
for p in pairs:
  result=max(find_sq(p),result)
print(result)
#pairs.sort(lambda a,b:len(a)-len(b))

