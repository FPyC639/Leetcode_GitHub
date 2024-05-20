# Intuition
My first thoughts in on the problem were to simply solve the as quickly one could code the problem in a timed environment.

# Approach
My approach to solving the problem is using brute force and it is based on a condition and looping over until that condition is met or otherwise return null.

# Complexity
- Time complexity:
The time complexity for the program is $$O(n^2)$$
because I am still iterating over two for loops.

- Space complexity:
The Space Complexity of this solution is according to ChatGPT $$O(n)$$
because the space is constant no matter the data.

# Code
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i,j]
        
```