from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x*x, nums)))
        

# Problem Link :https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/ not actually 
# Time Complexity : O(n) Not Actually 
print(Solution().sortedSquares([-4,-1,0,3,10]))