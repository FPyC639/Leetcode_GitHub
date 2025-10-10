**Time Complexity:**  
The algorithm uses binary search, so the time complexity is $O(\log x)$.

**Space Complexity:**  
The space complexity is $O(x)$ due to the creation of the range `ls = range(0, x+1)`.
```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        lft = 0
        rght = x
        ls = range(0,x+1)
        if x <= 0:
            return 0
        while lft <= rght:
            mid = (lft + rght) // 2
            if ls[mid] * ls[mid] == x:
                return mid
            elif ls[mid] * ls[mid] < x:
                lft  = mid + 1
            else:
                rght = mid - 1
        if rght * rght <= x:
            return rght
```