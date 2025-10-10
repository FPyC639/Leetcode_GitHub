class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        for i in range(0,x+1,1):
            hb = i*i
            lb = hb - 2*i - 1
            if hb == x:
                return i
            elif x in range(lb,hb):
                return i - 1
            else:
                pass
if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))