# Intuition
My first thoughts to solve this problem was not to search for values that were not present in the list to begin with so I decided to simply skip those values that are not in the list.

# Approach
The approach in this way allows one to not iterate over values that are not present in the situation.

# Complexity
- Time complexity:
The time complexity of the approach is still $$O(n^2)$$ because of the search through the list and the for loops.

- Space complexity:
The space complextity of the this problem is still $$O(1)$$

# Code
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if (target-nums[i]) not in nums:
                    continue
            for j in range(1,len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i,j]
        
```