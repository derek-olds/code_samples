#!/usr/bin/env python
# test for lightbulbs.py

import lightbulbs
import unittest


class LightbulbsTest(unittest.TestCase):
  """Tests the Lightbulbs module."""

  def test_recursive_function(self):
    """Tests the recursive solution to the lightbulb problem."""
    # Test basic functionality.
    self.assertEqual(lightbulbs.recursive_bulbs([1,1,0,1,0,1,1,0]), 5)

    # Test edge: All 1s.  
    self.assertEqual(lightbulbs.recursive_bulbs([1,1,1,1,1]), 0)

    # Test edge: All 0s.  
    self.assertEqual(lightbulbs.recursive_bulbs([0,0,0,0,0]), 1)
  
    # Test edge: One element 0.  
    self.assertEqual(lightbulbs.recursive_bulbs([0]), 1)

    # Test edge: One element 1.  
    self.assertEqual(lightbulbs.recursive_bulbs([1]), 0)

  def test_modulo_function(self):
    """Tests the modulo solution to the lightbulb problem."""
    # Test basic functionality.
    self.assertEqual(lightbulbs.modulo_bulbs([1,1,0,1,0,1,1,0]), 5)

    # Test edge: All 1s.  
    self.assertEqual(lightbulbs.modulo_bulbs([1,1,1,1,1]), 0)

    # Test edge: All 0s.  
    self.assertEqual(lightbulbs.modulo_bulbs([0,0,0,0,0]), 1)
  
    # Test edge: One element 0.  
    self.assertEqual(lightbulbs.modulo_bulbs([0]), 1)

    # Test edge: One element 1.  
    self.assertEqual(lightbulbs.modulo_bulbs([1]), 0)


if __name__ == "__main__":
  unittest.main()
