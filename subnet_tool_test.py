#!/usr/bin/python
"""Tests for subnet_tools.py"""

import unittest
import subnet_tool

class IsNetValidTest(unittest.TestCase):
    """Tests the is_net_valid functioni. Test will use the last available ip in
    the given subnet for True and the first unavalable ip in that subnet."""

    def test_class_a(self):
        """Test the function on a class A subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "8.0.0.0/8", "8.255.255.255"))
        self.assertFalse(subnet_tool.is_net_valid(
            "8.0.0.0/8", "9.0.0.1"))

    def test_subclassed_a(self):
        """Test the funtion on a subnetted class A subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "8.0.0.0/10", "8.63.255.255"))
        self.assertFalse(subnet_tool.is_net_valid(
            "8.0.0.0/10", "8.64.0.0"))

    def test_class_b(self):
        """Test the function on a class B subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "10.10.0.0/16", "10.10.255.255"))
        self.assertFalse(subnet_tool.is_net_valid(
            "10.10.0.0/16", "10.11.0.0"))

    def test_subclassed_b(self):
        """Test the funtion on a subnetted class B subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "10.10.0.0/18", "10.10.63.255"))
        self.assertFalse(subnet_tool.is_net_valid(
            "10.10.0.0/18", "10.10.64.0"))

    def test_class_c(self):
        """Test the function on a class C subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "192.168.1.0/24", "192.168.1.255"))
        self.assertFalse(subnet_tool.is_net_valid(
            "192.168.0.0/24", "192.168.2.0"))

    def test_subclassed_c(self):
        """Test the funtion on a subnetted class C subnet."""
        self.assertTrue(subnet_tool.is_net_valid(
            "192.168.1.0/25", "192.168.1.127"))
        self.assertFalse(subnet_tool.is_net_valid(
            "192.168.1.0/25", "192.168.1.128"))


if __name__ == "__main__":
    unittest.main()
