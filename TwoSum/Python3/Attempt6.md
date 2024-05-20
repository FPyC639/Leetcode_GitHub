# Intuition
Use the enumerate method to get the best possible solution to the probelm along with a dictionary.

# Approach
The approach for the problem consisters enumerating the list of nums to have a key, value pair and then iterate over them creating the list with the two sums.

# Complexity
- Time complexity:
The time complexity here is $$O(n)$$ because of the insertion operation on a hash table.

- Space complexity:
The space complexity for this particular solution is $$O(n)$$ because the worst case is that one inserts every value into the hash table.

# Code
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = enumerate(nums)
        num_dict = dict()
        for i, j in a:
            complement = target - j
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[j] = i
        return []
```