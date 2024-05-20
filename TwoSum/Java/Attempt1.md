# Intuition
My first thoughts about the problem lead to use the method described in the approach because it was the quickest way that I could solve the problem. I seek to improve on this solution with other data structures such as HashMaps and HashTables

# Approach
The approach is to use two for loops and iterate over them until a condition is met in which the operation ceases return the indices of the numbers in the array that provide the solution to the problem.

# Complexity
- Time complexity:
The time complexity of this problem according to ChatGPT 4 is $$O(n^2)$$
The reason being is that I am using two for loops that each time it iterates over n times amount of data.

- Space complexity:
Space complexity is approximately 1 because regardless of the input size the operations are still unaffected.

# Code
```Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i< nums.length; i++){
            for(int j = 1; j < nums.length; j++){
                if(i == j)
                    continue;
                if(nums[i]+nums[j] == target)
                    return new int[] {i,j};
            }
        }
        return null;
    }
}
```