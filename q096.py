#!/usr/bin/env python3
import lib
import copy

lines = open('p096_sudoku.txt').read().strip().split('\n')
grids = []
for i in range(len(lines)//10):
  lines.pop(0)
  grid = []
  for i in range(9):
    grid.append(list(map(int, list(lines.pop(0)))))
  grids.append(grid)

def valid(grid,i,j,n):
  if grid[i][j] != 0:
    raise Exception('pos not empty')
  for pp in range(9): # check rows and columns
    if grid[pp][j] == n or grid[i][pp] == n:
      return False

  isq = i - (i % 3)
  jsq = j - (j % 3)
  for ii in range(isq,isq+3):
    for jj in range(jsq,jsq+3):
      if grid[ii][jj] == n:
        return False
  return True

def empty_positions(grid):
  result = []
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        result.append((i,j))
  return result

def get_candidates(grid,i,j):
  result = []
  for n in range(1,10):
    if valid(grid,i,j,n):
      result.append(n)
  return result

def iterate(grid):
  # Fill cells that have only one possible value
  changed = True
  while changed:
    changed = False
    positions = empty_positions(grid)
    if not positions: # completed
      return grid

    for i,j in positions:
      candidates = get_candidates(grid,i,j)
      if len(candidates) == 1:
        grid[i][j] = candidates[0] 
        changed = True

  # Find cell with smallest number of candidates
  mn = 10
  mn_p = mn_c = None
  for i,j in positions:
    candidates = get_candidates(grid,i,j)
    ln = len(candidates)
    if ln > 0 and ln < mn:
      mn_p = i,j
      mn_c = candidates
      mn = ln

  if not mn_p:
    return None # no candidates

  # Back track on possible values for that cell
  i,j = mn_p
  for n in mn_c:
    nxt = copy.deepcopy(grid)
    nxt[i][j] = n
    result = iterate(nxt)
    if result:
      return result

sm = 0
for grid in grids:
  res = iterate(grid)
  sm += res[0][0]*100 + res[0][1]*10 +res[0][2]
print(sm)
