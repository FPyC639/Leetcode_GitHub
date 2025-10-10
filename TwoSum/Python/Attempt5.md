# Intuition
Use a different condition to test for to possibly improve the speed of the algorithm.

# Approach
The approach in this case was to reduce the amount of variables and calculations that were being done as well as provide a more efficent way in obtaining the answer.

# Complexity
- Time complexity:
The time complexity for this probelm is still $$O(n^2)$$ because of the list operations that are being used in this excercise.

- Space complexity:
The space complexity for this problem is still $$O(1)$$ because it returns a fixed list.

# Code
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        for i in range(a):
            b = target-nums[i]
            if b not in nums:
                continue
            else:
                for j in range(i+1,a):
                    if nums[j] == b:
                        return [i,j]
```