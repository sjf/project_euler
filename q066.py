#!/usr/bin/env python3
import lib
D=1
N=1000

def solve(d):
  # x = 2
  # # y**2 = (x**2 - 1) / D
  # while True:
  #   y2 = (x**2 - 1)/d
  #   if lib.isint(y2) and lib.isint(y2**0.5):
  #     print(x,"^2 -",d,'*',y2**0.5,'^2 = 1')
  #     return x
  #   x += 1
  x = 2
  # x**2-1 = Dn
  while True:
    dn = x**2-1
    if dn % d == 0:
      y2 = dn//d
      if lib.is_square(y2):
        return x
    x += 1

d = D
mx = (0,0) # x,d
while d < N:
  if not lib.is_square(d): # squares have no solution
    x,y = lib.solve_pells_equation(d) 
    if x > mx[0]:
      mx = (x,d)
    print(d,x)
  d += 1

print(mx)

