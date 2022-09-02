from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)-1
        print(length)
        while  length>-1 and length >= 0 :# while lenght != 0 
            if nums[length] == val:
                nums.remove(val)
            print(nums)
            length-=1
        return nums




           
if __name__ == '__main__':
    print(Solution().removeElement([3,2,2,3],3))
