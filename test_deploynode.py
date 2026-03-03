# test_deploynode.py
"""
Tests for DeployNode module.
"""

import unittest
from deploynode import DeployNode

class TestDeployNode(unittest.TestCase):
    """Test cases for DeployNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeployNode()
        self.assertIsInstance(instance, DeployNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeployNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
