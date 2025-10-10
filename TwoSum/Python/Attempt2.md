# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
The approach to the problem is based of the intutition that I believed that the problem would be probably best solved with a built-in function; however, it did not lead to a system improvement and in fact was highly similar to the first attempt.

# Complexity
- Time complexity:
The time complexity in this bit of code is also very similar to the first attempt and has a $$O(n^2)$$
for having a dual for loop structure.

- Space complexity:
The space complextity in this example is $$O(1)$$ due to it storing only a constant data.

# Code
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index1, value1 in enumerate(nums[1:], start=1):
                if index == index1:
                    continue
                if value + value1 == target:
                    return [index,index1]
```