from typing import List
class Solution:
        def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            """
            Do not return anything, modify nums1 in-place instead.
            """
            for k in range(m+n):
                if len(nums1)!=m:
                    nums1.pop()
                if len(nums2)!=n:
                    nums2.pop()
                if len(nums1) == m and len(nums2) == n:
                    break
            while nums2:
                insert = False 
                last = nums2.pop()
                for index,value in enumerate(nums1):
                    insert = False
                    if value >= last:
                        # print("insert here",last,value)

                        nums1.insert(index,last)
                        insert = True
                        break
                # print("append",last)
                if not insert:
                    nums1.append(last)




# Learning : Why nums1 = nums[:m] was not working ? 
# What to do when brain freeze happens . Exercise or Meditation 