########## Hi there ######################s
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead."""
        #Can you come up with an algorithm that runs in O(m + n) time?

        p1 = m-1 
        p2 = n-1 
        pf = (n+m)-1 
        
        if p1 < 0:
            nums1[:n] = nums2
            return

        while p1 >= 0 and p2 >= 0: 
            
            if nums1[p1] >= nums2[p2]: 
                nums1[pf] = nums1[p1]
                p1 -= 1 
                pf -= 1 
            else: 
                nums1[pf] = nums2[p2]
                p2-= 1 
                pf -= 1

        if  p1 < 0:
            nums1[:pf+1] = nums2[:p2+1]
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  

