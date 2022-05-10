import unittest
import filter

class TestCases(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

   def test_greater1(self):
      nums = [1.1, 2.2, 2345]
      n = 0

      greater = filter.are_greater_than_n(nums, n)
      self.assertListAlmostEqual(greater, [1.1, 2.2, 2345])

   def test_greater12(self):
      nums = [-1, 2.5, 1034, 100, 101, 192]
      n = 100

      greater = filter.are_greater_than_n(nums, n)
      self.assertListAlmostEqual(greater, [1034, 101, 192])

   def test_div1(self):
      nums = [-1, 2.5, 1034, 100, 101, 192, -100]
      n = 100

      div = filter.are_divisible_by_n(nums, n)
      self.assertListAlmostEqual(div, [100, -100])

   def test_div2(self):
      nums = [-4, 0, 2, 23456, 100]
      n = 2
      div = filter.are_divisible_by_n(nums, n)
      self.assertListAlmostEqual(div, [-4, 0, 2, 23456, 100])

   def test_pos1(self):
      nums = [-1, -100, 1, 39, 0, 9]
      
      positive = filter.are_positive(nums)
      self.assertListAlmostEqual(positive, [1,39,9])

   def test_pos2(self):
      nums = [-10000, -500, -1, 4, 3, 9991]
      
      positive = filter.are_positive(nums)
      self.assertListAlmostEqual(positive, [4,3,9991])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

