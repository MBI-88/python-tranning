import unittest
from bubblesort import bubblesort


class TestBubbleSort(unittest.TestCase):

    def test_bubblesort(self):
        result = [4,5,7,8,9,10,23,45]
        test = [5,4,8,7,9,10,23,45]
        self.assertEqual(bubblesort(test), result)



if __name__ == "__main__":
    unittest.main()