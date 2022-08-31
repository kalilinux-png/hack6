from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0 
        while nums:
            number = nums.pop()
            count=0
            while number>0:
                number//=10
                count +=1
            if count%2==0:
                even +=1
        return even 

    




        