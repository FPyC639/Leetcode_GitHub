Finds the first bad version in a sequence of versions using a recursive binary search approach.

Methods:
    binarySearchRecurse(lft, rght):
        Recursively performs binary search between indices `lft` and `rght` to locate the first bad version.
        Calls the external function `isBadVersion(mid)` to check if a version is bad.
        Returns the index of the first bad version.

    firstBadVersion(n):
        Initializes the search boundaries and invokes the recursive binary search.
        Returns the index of the first bad version in the range [1, n].

Space Complexity Analysis:
    - The space complexity is O(log n) due to the recursion stack in binarySearchRecurse, where n is the number of versions.

Time Complexity Analysis:
    - The time complexity is O(log n) because each recursive call halves the search space, similar to standard binary search.
```Python
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
```