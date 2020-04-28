import unittest
from sortalgorithm import SortAlgorithm

class TestSort(unittest.TestCase):
    def test_BubbleSort(self):
        SortObj = SortAlgorithm()
        result = SortObj.BubbleSort([10,7,8,4,3,6,9,5,1,2])
        self.assertSequenceEqual(result,[1,2,3,4,5,6,7,8,9])
    def test_SelectSort(self):
        SortObj = SortAlgorithm()
        result = SortObj.SelectSort([10,7,8,4,3,6,9,5,1,2])
        self.assertSequenceEqual(result,[1,2,3,4,5,6,7,8,9,10])
