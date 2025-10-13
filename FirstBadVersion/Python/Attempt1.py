# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from math import floor
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lft = 1
        rght = n
        while lft <= rght:
            mid = floor((lft + rght) // 2)
            mid_check = isBadVersion(mid)
            if mid_check == True:
                rght = mid - 1
            else:
                lft = mid + 1
        return lft
def isBadVersion(version: int) -> bool:
    # API Simulation
    pass