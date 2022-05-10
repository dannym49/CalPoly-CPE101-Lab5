nums = [1,2,3,4,5,6,7,8]
def square_all(nums):
   i = 0
   square = []
   while i < len(nums):
      square.insert(i, nums[i]**2) 
      i+=1
   return square

def add_n_all(nums, n):
   sum_nums = [num+n for num in nums]
   return sum_nums   

def even_or_odd_all(nums):
   evens = []
   for num in nums:
      if num % 2 == 0:
         num = True
         evens.append(num)
      else:
         num = False
         evens.append(num)
   return evens



