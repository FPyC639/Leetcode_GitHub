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
        