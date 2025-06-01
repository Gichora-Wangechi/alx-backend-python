#!/usr/bin/env python3 """Unit and Integration Tests for utils.py"""

import unittest 
from parameterized import parameterized 
from unittest.mock import patch, Mock 
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase): 
    """Tests for access_nested_map function."""

@parameterized.expand([ 
    ("nested_map with 1-level key", {"a": 1}, ("a",), 1), 
    ("nested_map with 2-levels key", {"a": {"b": 2}}, ("a",), {"b": 2}), 
    ("nested_map full path", {"a": {"b": 2}}, ("a", "b"), 2), 
]) 
def test_access_nested_map(self, _, nested_map, path, expected): 
    """Test correct output for access_nested_map.""" 
    self.assertEqual(access_nested_map(nested_map, path), expected) 
    
@parameterized.expand([ 
    ("empty map", {}, ("a",), "a"), 
    ("missing nested key", {"a": 1}, ("a", "b"), "b"), 
]) def test_access_nested_map_exception(self, _, nested_map, path, expected_key): 
    """Test that KeyError is raised with correct message.""" 
    with self.assertRaises(KeyError) as context: 
        access_nested_map(nested_map, path) 
        self.assertEqual(str(context.exception), f"'{expected_key}'") 

class TestGetJson(unittest.TestCase): 
    """Tests for get_json function."""
    
    @parameterized.expand([ 
        ("http://example.com", {"payload": True}), 
        ("http://holberton.io", {"payload": False}) ]) 
    def test_get_json 
