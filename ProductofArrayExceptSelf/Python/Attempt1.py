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