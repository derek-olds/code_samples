#!/usr/bin/env python
"""Test for the diagonals.py"""

import diagonals
import unittest


class DiagonalsTest(unittest.TestCase):
  """Tests the diagonals module."""

  def test_anti_diagonal(self):
    """Tests the anti_diagonal function. (Left high to right low)"""
    input_array = [[1,2,3],[4,5,6],[7,8,9]]
    return_array = [[7],[4,8],[1,5,9],[2,6],[3]]
    self.assertEqual(diagonals.anti_diagonal(input_array), return_array)

  def test_diagonal(self):
    """Tests the diagonal function. (Left low to right high)"""
    input_array = [[1,2,3],[4,5,6],[7,8,9]]
    return_array = [[1],[2,4],[3,5,7],[6,8],[9]]
    self.assertEqual(diagonals.diagonal(input_array), return_array)


if __name__ == "__main__":
  unittest.main()
