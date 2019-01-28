#!/usr/bin/env python
# Module for working through the lightbulbs programming problem.
# Given a list of lightbulbs that can be on or off, return the number
# of switches needed to turn them all on. Each change in state will change
# the state of all bulbs to the right of the current bulb.

def recursive_bulbs(bit_list, count=0):
  """This function solves the problem using brute force and recursion. This
  seems to be an example of a case where you shouldn't use recursion. I estimate  speed and and memory to be O(n!).

  Arguments:
    bit_list: list, list of ones and zeroes that represent lightbulbs.
    count: int, the number of times a bit switch has been done. Default is
           zero. This value should only be used by the recursion logic.

  Returns:
    count: int, number of opperations needed to switch all bits to one.
  """
  if len(bit_list) == 1:
    if bit_list[0] == 1:
      return count
    else:
      return count + 1
  else:
    for pos, value in enumerate(bit_list):
      if value == 0:
        new_bit_list = bit_list[pos:]
        for new_list_pos, new_value in enumerate(new_bit_list):
          if new_value == 1:
            new_bit_list[new_list_pos] = 0
          else:
            new_bit_list[new_list_pos] = 1
        return recursive_bulbs(new_bit_list, count + 1)
    return count

def modulo_bulbs(bit_list):
  """This function solves the problem using the formula (val + count) % 2. As
  you parse the list left to right, if val + count is divisible by two then the
  count is incremented. This is much more efficient. It is O(n) for speed, and
  O(1) for memory.

  Arguments:
    bit_list: list, list of ones and zeroes that represent lightbulbs.

  Returns:
    count: int, number of opperations needed to switch all bits to one.
  """
  count = 0
  for val in bit_list:
    if (val + count) % 2 == 0:
      count += 1
  return count
