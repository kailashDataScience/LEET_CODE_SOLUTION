class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       for i in range(len(nums)-1):
           print (nums[i])
        
           for j in range(1,len(nums)):
               if i==j:
                   continue
           
               if nums[i]+nums[j]==target:

                        answer=(i,j)
                        return list(answer)
                    
                
                   