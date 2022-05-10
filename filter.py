
def are_positive(nums):
   i = 0
   positive = []
   while i < len(nums):
      if nums[i] > 0:
         positive.insert(i, nums[i]) 
      i+=1
   return positive

def are_greater_than_n(nums, n):
   greater = [num for num in nums if num > n]
   return greater


def are_divisible_by_n(nums, n):
   div = []
   for num in nums:
      if num % n == 0:
         div.append(num)
   return div

