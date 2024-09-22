import unittest 
from sort import sortfrequency


class TestSortFrecuency(unittest.TestCase):

    def test_sortfrecuency_1(self):
        test = "eert"
        self.assertEqual(sortfrequency("tree"), test)
    
    def test_sortfrecuency_2(self):
        test = "aaaccc"
        self.assertEqual(sortfrequency("cccaaa"),test)
    
    def test_sortfrecuency_3(self):
        test = "bbAa"
        self.assertEqual(sortfrequency("Aabb"),  "abbA")



if __name__ == "__main__":
    unittest.main()