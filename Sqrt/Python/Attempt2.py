class Solution:
    def mySqrt(self, x: int) -> int:
        lft = 0
        rght = x
        ls = range(0,x+1)
        if x <= 0:
            return 0
        while lft <= rght:
            mid = (lft + rght) // 2
            if ls[mid] * ls[mid] == x:
                return mid
            elif ls[mid] * ls[mid] < x:
                lft  = mid + 1
            else:
                rght = mid - 1
        if rght * rght <= x:
            return rght
if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))