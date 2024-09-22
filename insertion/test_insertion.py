import unittest
from insertion import insertionsort



class TestInsertion(unittest.TestCase):

    def test_insertion(self):
        test = [10,20,1,5,8,3,7,21,100,23,9]
        result = [1,3,5,7,8,9,10,20,21,23,100]
        self.assertEqual(insertionsort(test), result)


if __name__ == '__main__':
    unittest.main()