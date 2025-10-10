## Time and Space Complexity Analysis

### Time Complexity
The code iterates from `0` to `x` (inclusive) in a for loop. In the worst case, it performs `O(x)` iterations. Each iteration does constant work, so the overall time complexity is **O(x)**.

### Space Complexity
The algorithm uses a constant amount of extra space for variables (`i`, `hb`, `lb`). Therefore, the space complexity is **O(1)**.

```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        for i in range(0,x+1,1):
            hb = i*i
            lb = hb - 2*i - 1
            if hb == x:
                return i
            elif x in range(lb,hb):
                return i - 1
            else:
                pass
```