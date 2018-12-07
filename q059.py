#!/usr/bin/env python3
import lib
import string
txt = open('p059_cipher.txt').read()
nums = list(map(int,txt.split(',')))

def ok(c):
  return c in string.printable

def decrypt(nums,key):
  res = ""
  for i in range(len(nums)):
    c = chr(nums[i] ^ key[i%3])
    if not ok(c):
      return None
    res += c
  return res

# for a in string.ascii_lowercase:
#   for b in string.ascii_lowercase:
#     for c in string.ascii_lowercase:
#       key = [ord(a),ord(b),ord(c)]
#       res = decrypt(nums,key)
#       if res:
#         print(key, res)

key=[103, 111, 100]
txt = decrypt(nums,key)
print(sum(map(ord,txt)))