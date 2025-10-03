class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = self.convert2str(x)
        b = self.helperfunc(a)
        return self.final(a,b)
    def convert2str(self, x:int) -> str:
        return str(x)
    def helperfunc(self, x:str) -> str:
        return x[::-1]
    def final(self, x:str, y:str) -> bool:
        return x == y
if __name__ == "__main__":
    x = 121
    sol = Solution()
    print(sol.isPalindrome(x))