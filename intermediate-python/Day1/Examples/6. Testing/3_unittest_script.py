import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,4,5]),10,'1 + 4 + 5 must be 10')

    
if __name__ == '__main__':
    unittest.main()