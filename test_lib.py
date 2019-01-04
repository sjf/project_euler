import pytest
from lib import *

#### Geometric numbers ####

def test_triangle():
  assert triangle(0) == 0
  assert triangle(1) == 1
  assert triangle(2) == 3
  assert triangle(10) == 55

def test_square():
  assert square(0) == 0
  assert square(1) == 1
  assert square(2) == 4
  assert square(10) == 100


def test_pentagonal():
  assert pentagonal(0) == 0
  assert pentagonal(1) == 1
  assert pentagonal(2) == 5
  assert pentagonal(10) == 145

def test_gpentagonal():
  assert gpentagonal(0) == 0
  assert gpentagonal(1) == 1
  assert gpentagonal(2) == 2
  assert gpentagonal(10) == 40

def test_hexagonal():
  assert hexagonal(0) == 0
  assert hexagonal(1) == 1
  assert hexagonal(2) == 6
  assert hexagonal(10) == 190

def test_heptagonal():
  assert heptagonal(0) == 0
  assert heptagonal(1) == 1
  assert heptagonal(2) == 7
  assert heptagonal(10) == 235

def test_octagonal():
  assert octagonal(0) == 0
  assert octagonal(1) == 1
  assert octagonal(2) == 8
  assert octagonal(10) == 280

def test_is_triangular():
  assert is_triangular(0) == True
  assert is_triangular(1) == True
  assert is_triangular(10) == True
  assert is_triangular(5) == False

def test_is_square():
  assert is_square(0) == True
  assert is_square(1) == True
  assert is_square(9) == True
  assert is_square(5) == False

def test_is_cube():
  assert is_cube(0) == True
  assert is_cube(1) == True
  assert is_cube(27) == True
  assert is_cube(12) == False

def test_is_pentagonal():
  assert is_pentagonal(1) == True
  assert is_pentagonal(35) == True
  assert is_pentagonal(15) == False

def test_is_hexagonal():
  assert is_hexagonal(1) == True
  assert is_hexagonal(45) == True
  assert is_hexagonal(44) == False

#### Graph operations ####

def test_topological_sort():
  assert topological_sort([1,2,3],{1:[2,3],2:[3]}) == [1,2,3]

#### List operations ####

def test_multiply():
  assert multiply([1,2,3]) == 6

def test_first():
  assert first([1,2,3]) == 1

def test_second():
  assert second([1,2,3]) == 2

def test_push():
  assert push([1,2,3], 0) == [0,1,2,3]

def test_nub2d():
  assert nub2d([[1,2],[1,2],[3,4],[5,6],[6,5]]) == [(1,2),(3,4),(5,6),(6,5)]

def test_reversel():
  assert reversel([1,2,3,4]) == [4,3,2,1]
  assert reversel([1,2,3,4],0,4) == [4,3,2,1]
  assert reversel([1,2,3,4],0,2) == [2,1,3,4]
  assert reversel([1,2,3,4],1,3) == [1,3,2,4]
  assert reversel([1,2,3,4],2,4) == [1,2,4,3]

def test_take():
  assert take([1,2,3,4],0) == []
  assert take([1,2,3,4],2) == [1,2]
