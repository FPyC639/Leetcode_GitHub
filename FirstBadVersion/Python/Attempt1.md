Finds the first bad version in a sequence of versions using binary search.

Args:
    $n$ (int): The total number of versions.

Returns:
    $int$: The version number of the first bad version.

Time Complexity:
    $O(\log n)$ - The binary search reduces the search space by half each iteration.

Space Complexity:
    $O(1)$ - Only a constant amount of extra space is used.

```Python
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
```