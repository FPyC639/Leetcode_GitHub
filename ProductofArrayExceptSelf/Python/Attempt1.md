## Product of Array Except Self

This code implements a solution to the "Product of Array Except Self" problem.  
Given an array `nums`, it returns a new array such that each element at index `i` is the product of all the numbers in the original array except `nums[i]`.  
The solution uses prefix and suffix products to achieve this in O(n) time without using division.

- **Prefix pass:** Computes the product of all elements to the left of each index.
- **Suffix pass:** Multiplies each element by the product of all elements to the right.

### Time and Space Complexity

- **Time Complexity:** O(n), where n is the length of the input array. The algorithm makes two passes through the array.
- **Space Complexity:** O(1) extra space (excluding the output array), since the output array does not count towards extra space as per the problem's constraints.


```Python
from math import prod
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # left (prefix) products
        p = 1
        for i in range(n):
            print(f"Left product at index {i}: {p}")
            res[i] = p
            p *= nums[i]
        print(f"Left products: {res}")
        # right (suffix) products
        p = 1
        for i in range(n - 1, -1, -1):
            print(f"Right product at index {i}: {p}")
            res[i] *= p
            p *= nums[i]
        print(f"Right products: {res}")
        return res
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
```