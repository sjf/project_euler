#!/usr/bin/env python3
import lib
from collections import defaultdict

nums = open('p079_keylog.txt').read().strip().split('\n')
lines = list(map(lambda x:list(map(int, list(x))),nums))
nums = {}
for line in lines:
  for d in line:
    nums[d] = True

nodes=list(nums.keys())
nodes.sort()
edges = defaultdict(set)
for line in lines:
  a,b,c = line
  edges[a].add(b)
  edges[b].add(c)
    
print(lib.topological_sort(nodes,edges))

