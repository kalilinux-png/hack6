from typing import List 
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         db = { }   # to store unique elements 
#         end  = len(nums)-1 
        
#         while end!=-1: # because we need 0 index also 

#             if nums[end] in db:
#                 nums.pop(end)
#             else:
#                 db[nums[end]] = True
#             end-=1
#         print(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0 
        
        j=0
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i] # what does this mean 
                
        return j+1



# better code from leetcode 

"""class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0 
        
        j=0
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i] # what does this mean 
                
        return j+1"""


            
# Learning : Use Debugger to better understand other's code don't just try to assume 

if __name__=="__main__":
    Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])


        