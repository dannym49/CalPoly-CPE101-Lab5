import unittest
import map

class TestCases(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

   def test_square1(self):
      # Add code here.
      nums = [1,2,3,4,5]
      square = map.square_all(nums)
      self.assertListAlmostEqual(square, [1,4,9,16,25])

   def test_square2(self):
      # Add code here.
      nums = [2,50,100,3]
     
     
      square = map.square_all(nums)
      self.assertListAlmostEqual(square, [4, 2500, 10000, 9])

   def test_add1(self):
      # Add code here.
      nums = [1,2,3,4,5]
      n = 4
     
      sums = map.add_n_all(nums,n)
      self.assertListAlmostEqual(sums, [5,6,7,8,9])

   def test_add2(self):
      # Add code here.
      nums = [10,30,12,9]
      n = 50
      
      sums = map.add_n_all(nums,n)
      self.assertListAlmostEqual(sums, [60,80,62,59])

   def test_even1(self):
      # Add code here.
      nums = [1,2,3,4,5,6,7]
      
      evens = map.even_or_odd_all(nums)
      self.assertListAlmostEqual(evens, [False,True,False,True,False,True,False])

   def test_even2(self):
      # Add code here.
      nums = [9,3,5,4,6,10,1002]
      
      evens = map.even_or_odd_all(nums)
      self.assertListAlmostEqual(evens, [False,False,False,True,True,True,True])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

