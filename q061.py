#!/usr/bin/env python3
import lib

fs=[lib.triangle, lib.square, lib.pentagonal, lib.hexagonal, lib.heptagonal, lib.octagonal]
nums=[]
# Get all four digit candidates for each type of number
for i in range(len(fs)):
  f = fs[i]
  result = []
  nums.append(result)

  i = 1
  val = f(i)
  while lib.num_digits(val) < 5:
    if lib.num_digits(val) == 4 and \
     val % 100 != 0 and lib.get_digit(val,1) != 0:
      result.append(val)
    i += 1
    val = f(i)

# Build a table of prefixes for each set of numbers. 
prefixes=[]
for numl in nums:
  d = {}
  prefixes.append(d)
  for num in numl:
    key = num//100
    if not key in d:
      d[key] = []
    d[key].append(num)

def matches(num, indexes, prefixes):
  """ Returns sequences of numbers where the last 2 digits of a number and the first two 
      digits of the preceeding number, using the list of prefixes according to the order
      given in indexes. `num` is the first number in the sequence. """
  if not indexes:
    return [num]
  indexes = indexes[:]
  i = indexes.pop(0)
  d = prefixes[i]
  key = num%100
  if not key in d or not d[key]:
    return None

  nxtl = d[key]
  for nxt in nxtl:
    res = matches(nxt, indexes, prefixes)
    if res:
      return [num] + res
  return None

prefixes.append({})
for indexes in lib.permutations(list(range(6))):
  i = indexes.pop(0)
  indexes.append(6)
  numl = nums[i]

  for num in numl:
    d = {num // 100 : [num % 100]} # final num must be prefix of the first number
    prefixes[6] = d
    res = matches(num, indexes, prefixes)
    if res:
      result = sum(res[:6])
      print(result, res,[i] + indexes)

