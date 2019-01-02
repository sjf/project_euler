#!/usr/bin/env python3
import lib

def add(a,b):
  if a is None or b is None:
    return None
  return a+b

def sub(a,b):
  if a is None or b is None:
    return None
  return a-b

def mul(a,b):
  if a is None or b is None:
    return None
  return a*b

def div(a,b):
  if b == 0 or a is None or b is None:
    return None
  return a/b

def brackets(a,b,c,d,x,y,z):
  results = []
  #a.(b.(c.d))
  results.append(x(a, y(b, z(c,d))))
  #a.((b.c).d)  
  results.append(x(a, z(y(b, c), d)))
  #(a.b).(c.d)
  results.append(y(x(a, b), z(c,d)))
  #((a.b).c).d)
  results.append(z(y(x(a, b), c),d))
  #(a.(b.c)).d)
  results.append(z(x(a, y(b, c)), d))
  return results

def ln_consecutive(l):
  count = mx = 1
  for i in range(1, len(l)):
    if l[i-1] + 1 == l[i]:
      count += 1
      mx = max(count,mx)
    else:
      count = 1
  return mx

mx = 0
mx_n = []
for numbers in lib.subsets(list(range(1,10)), 4):
  results = set()
  for orderednumbers in lib.permutations_lexico(numbers):
    for ops in lib.combinations([add,sub,mul,div], 3):
      for result in brackets(*orderednumbers, *ops):
        if result is not None and lib.is_int(result) and result > 0:
            results.add(int(result))
  results = list(results)
  results.sort()
 
  ln = ln_consecutive(results)
  print(numbers, ln)
  if ln > mx:
    mx = max(ln,mx)
    mx_n = numbers

print('max', mx)
print(mx_n)


  