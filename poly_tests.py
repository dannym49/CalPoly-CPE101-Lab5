import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)


    # Add tests here
    def test1(self):
        self.assertListAlmostEqual([1,2],[1,2])
    def test_add1(self):
      poly1 = [2.3, 4.7, 1.0]
      poly2 = [1.2, 2.1, -3.2]

      poly3 = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
    def test_add2(self):
      poly1 = [5.9, 12, 1.0]
      poly2 = [2.2, 1.4, -5.0]

      poly3 = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [8.1, 13.4, -4.0])
    def test_mult1(self):
      poly1 = [5.9, 12, 1.0]
      poly2 = [2.2, 1.4, -5.0]

      poly3 = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [12.98, 34.66, -10.5, -58.6, -5])
if __name__ == '__main__':
    unittest.main()
