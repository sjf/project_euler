# -*- coding: utf-8 -*-

from functools import reduce
from collections import Counter
from collections import defaultdict
from collections import MutableMapping
from math import sqrt

#### Prime numbers ####

def prime_factors(n):
  """ Returns the prime factors of n."""
  assert isinstance(n, int)

  result = []
  p=2
  while p**2 <= n:
    if n % p == 0:
      result.append(p)
      n /= p
    else:
      p += 1
  result.append(int(n))
  return result

def factors(n):
  """ Returns the factors of n."""
  assert isinstance(n, int)
  if n == 1: return [1]
  # Get the prime factors of n, in the form p1^a, p2^b, p3^c
  prime_facs = Counter(prime_factors(n))
  # The factors of n are formed from every combination of the prime exponents
  return _factors(list(prime_facs.items()))

def _factors(pairs, partial=1):
  """ Return all factors from pairs of the prime factors and their exponents."""
  if not pairs:
    return [partial]
  result = []
  (num, exp) = pairs[0]
  for i in range(exp+1):
    result.extend(_factors(pairs[1:], partial * num**i))
  return result

def primes(n, sieve = None):
  """ Returns the prime numbers up to n."""
  assert isinstance(n, int)
  assert sieve is None or len(sieve) >= n 

  if not sieve:
    sieve = prime_sieve(n)
  result = []
  for i in range(2, n):
    if sieve[i]:
      result.append(i)
  return result

def prime_sieve(n):
  assert isinstance(n, int)
  # Sieve of Eratosthenes
  sieve = [True for i in range(0, n)]
  sieve[0] = sieve[1] = False # 1 is not prime
  for i in range(2, n):
    if sieve[i]:
      mul = 2
      while mul*i < n:
        sieve[mul*i] = False
        mul += 1
  return sieve

class Sieve(MutableMapping):
  def __init__(self, limit):
    self.store = dict()
    self.limit = limit

  def __getitem__(self, key):
    if key in self.store: #return stored value
      return self.store[key] 
    if key < self.limit: #return default value
      return True 
    # calculate value
    value = is_prime(key) 
    self.store[key] = value
    return value

  def __setitem__(self, key, value):
    self.store[key] = value

  def __delitem__(self, key):
    del self.store[key]

  def __iter__(self):
    return iter(self.store)

  def __len__(self):
    return self.limit

def sparse_prime_sieve(n):
  """ Returns a dictionary-like object that contains True for prime keys.
      Values for numbers up to n are stored in the dictionary. Accessing
      keys greater than n will calculate the result."""
  assert isinstance(n, int)
  sieve = Sieve(n)
  sieve[0] = sieve[1] = False # 1 is not prime
  # Sieve of Eratosthenes
  for i in range(2, n):
    if sieve[i]:
      mul = 2
      while mul*i < n:
        sieve[mul*i] = False
        mul += 1
  return sieve

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
_known_primes = [2, 3]
_rt_is_initialiased = False
def is_prime_mr(n, _precision_for_huge_n=16):
  """ Rabin miller primality test. """
  if not _rt_is_initialiased:
    _known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
    _rt_is_initialiased = True

  if n in (0, 1):
    return False
  if n in _known_primes:
    return True
  if any((n % p) == 0 for p in _known_primes):
    return False
    
  d, s = n - 1, 0
  while not d % 2:
    d, s = d >> 1, s + 1
  # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
  if n < 1373653: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3))
  if n < 25326001: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
  if n < 118670087467: 
    if n == 3215031751: 
      return False
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
  if n < 2152302898747: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
  if n < 3474749660383: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
  if n < 341550071728321: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
  # otherwise
  return not any(_try_composite(a, d, n, s) 
                 for a in _known_primes[:_precision_for_huge_n])

def is_prime_trial_division(n):
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False

  mx = n**0.5
  f=5
  inc = 2
  while f <= mx:
    if n % f == 0:
      return False
    f += inc
    inc = 6-inc #alternate 2,4
  return True

#### Permutations ####

def permutations(l):
  """ Generate the permutations of l using recursion. """
  if not l:
    return [[]]
  result = []
  for i in range(len(l)):
    item = l.pop(i)
    temp_result = permutations(l)
    l.insert(i,item)
    for res in temp_result:
      res.append(item)
    result.extend(temp_result)
  return result

def combinations(l,ln, partial=[]):
  """ Generate all permutations of length l using elements from l. """

  if len(partial) == ln:
    return [partial]
  results = []
  for x in l:
    np = partial[:]
    np.append(x)
    results.extend(combinations(l,ln,np))
  return results

def _max_movable(l,d):
  mx = None
  for i in range(len(l)-1):
    n = l[i]
    if d[i] == 1 and n > l[i+1]: #right
      if mx is None or n > l[mx]:
        mx = i
  for i in range(1,len(l)):
    n = l[i]
    if d[i] == -1 and n > l[i-1]: #left
      if mx is None or n > l[mx]:
        mx = i
  return mx

def permutations_sjt(l):
  """ Returns a generator that yields the permutations of l using
      the Steinhaus–Johnson–Trotter algorithm. """
  l.sort()
  yield l[:]
  # direction of each element
  d = [-1 for i in range(len(l))] # -1 = left
  # get index of largest moveable item (item is > than item it is facing)
  mx = _max_movable(l,d)  
  while mx is not None:
    n = l[mx]
    # Swap the largest item with the item it's facing
    if d[mx] == 1: # right
      l[mx],l[mx+1] = l[mx+1],l[mx]
      d[mx],d[mx+1] = d[mx+1],d[mx]
    else: # left
      l[mx-1],l[mx] = l[mx],l[mx-1]
      d[mx-1],d[mx] = d[mx],d[mx-1]
    # reverse the direction of all larger items
    for i in range(len(l)):
      if l[i] > n:
        d[i] *= -1

    yield l[:]
    mx = _max_movable(l,d) 

#### Digit operations ####

def num_digits(n):
  if n == 0:
    return 1
  c = 0
  while n:
    n = n//10
    c += 1
  return c

def to_digits(d):
  if d == 0: return [0]
  result = []
  while d:
    result.append(d % 10)
    d = d//10
  result.reverse()
  return result

def to_num(l):
  n = 0
  for i in l:
    n *= 10
    n += i
  return n

def set_digit(n,pos,d):
  n -= (n%10**(pos+1) - n%10**(pos)) 
  n += 10**pos * d
  return n

def get_digit(n,pos):
  return (n%10**(pos+1) - n%10**(pos)) // 10**pos 

def reverse(n):
  if n < 10:
    return n
  res = 0
  while n:
    res *= 10
    res += n%10
    n = n // 10
  return res

def concat(a,b):
  return a*10**num_digits(b) + b

def is_palindrome(n):
  return n == reverse(n)

def is_pandigital(n):
  if n == 0:
    return False
  # for each digit d of n, the binary digit in position d will be
  # set to 1.
  accum = 0
  # target will have binary digit set to 1 in each position
  # 1-number of digits in n
  target = 0
  while n:
    d = n %10
    n = n//10
    accum |= 1 << d
    target = (target << 1) | 1
  target = target << 1 # right shift one for zero digit position

  return accum == target

def isint(n):
  return n == int(n)

#### Geometric numbers ####

def triangle(n):
  return n*(n + 1)//2
def pentagonal(n):
  return n*(3*n-1)//2
def hexagonal(n):
  return n*(2*n - 1)
def is_triangular(x):
  n = (sqrt(8*x + 1) - 1) / 2
  return isint(n)
def is_pentagonal(x):
  n = (sqrt(24*x + 1) + 1) / 6
  return isint(n)
def is_hexagonal(x):
  n = (sqrt(8*x + 1) + 1) / 4
  return isint(n)

#### Graph operations ####

def topological_sort(nodes,edges):
  """ Topological sort of a DAG using Kahns algorithm.
      Nodes is a list of nodes in the graph. Edges is a dictionatory
      of the form d[node] = set(destination nodes). """
  iedges = defaultdict(set) # internal copy of the edges
  backedges = defaultdict(set)
  for a,dsts in edges.items():
    iedges[a] = set(dsts)
    for b in dsts:
      backedges[b].add(a)

  start = []
  for n in nodes:
    if len(backedges[n]) == 0:
      start.append(n)

  result = []
  while start:
    a = start.pop()
    result.append(a)
    nxts = set(iedges[a])
    for b in nxts:
      iedges[a].remove(b)
      backedges[b].remove(a)
      if len(backedges[b]) == 0:
        start.append(b)
  for es in iedges.values():
    if len(es) != 0:
      raise Exception('graph has a loop')
  return result

#### List operations ####

def multiply(l):
  assert isinstance(l, list)
  return reduce(lambda x, y: x*y, l)
def first(p):
  return p[0]
def second(p):
  return p[1]
def push(l, item):
  l.insert(0, item)
  return l
def print2d(l):
  print(",\n".join(map(str, l)))
def nub2d(l):
  return list(set(map(tuple,l)))

#### File Operations ####

def read_words_from_file(f):
  """ Reads a text file of words in the format '"word1","word2","word3"' """
  txt = open(f).read()
  return list(map(lambda s: s.strip('"'), txt.split(",")))

def sum_words(words):
  """ Returns the ascii sum of the the letters in each word in words. 
      Expects only capital letters. """
  return list(map(lambda s: sum(map(lambda c: ord(c) - ord('A') + 1, s)), words))

#### END ####
