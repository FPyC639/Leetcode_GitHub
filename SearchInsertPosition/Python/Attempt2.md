Searches for the target value in a sorted list and returns its index if found; otherwise, returns the index where it should be inserted to maintain order.

Args:
    nums (List[int]): A sorted list of integers.
    target (int): The value to search for.

Returns:
    int: The index of the target if found, or the index where it should be inserted.

Time Complexity: O(log n), where n is the length of nums.
Space Complexity: O(1), as only a constant amount of extra space is used.

```Python
from math import floor
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lft = 0
        rght = len(nums) - 1
        while(lft<=rght):
            mid = floor((lft + rght) / 2)
            if  nums[mid] == target:
                return mid
            elif target < nums[mid]:
                rght = mid - 1
            else:
                lft = mid + 1
        return lft 
```