class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement =  target - nums[i]
            if nums[i] in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i
                
  
        
