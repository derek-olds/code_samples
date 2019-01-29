#!/usr/bin/env python
"""Study of the diagonals interview question."""

#TODO(derek-olds): Make this work.
def anti_diagonal(input_array):
  size = len(input_array[0])
  ret = [0] * (2 * size - 1)
  for index in range(2 * size -1):
    ret[index] = []
  for y in range(size - 1, -1, -1):
    for x in range(size -1, -1, -1):
      ret[x+y].append(input_array[y][x])
  return ret

def diagonal(input_array):
  size = len(input_array[0])
  ret = [0] * (2 * size - 1)
  for index in range(2 * size - 1):
    ret[index] = []
  for y in range(size):
    for x in range(size):
      ret[x+y].append(input_array[y][x])
  return ret

