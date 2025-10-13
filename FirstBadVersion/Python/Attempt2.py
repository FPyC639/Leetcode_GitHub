# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from math import floor
class Solution:
    def binarySearchRecurse(self,lft, rght):
        if lft > rght:
            return lft
        mid = floor((lft + rght) // 2)
        mid_check = isBadVersion(mid)
        if mid_check:    
            return self.binarySearchRecurse(lft, mid - 1)
        else:
            return self.binarySearchRecurse(mid + 1, rght)
    def firstBadVersion(self, n: int) -> int:
        lft = 1
        rght = n
        return self.binarySearchRecurse(lft,rght)
def isBadVersion(version: int) -> bool:
    # API Simulation
    pass