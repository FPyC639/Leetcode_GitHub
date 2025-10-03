### Time Complexity

The main operation in the code is reversing a string and comparing it to the original. Converting an integer to a string (`str(x)`) takes O(n) time, where n is the number of digits in `x`. Reversing the string (`x[::-1]`) also takes O(n) time. The final comparison (`x == y`) takes O(n) time as well. Therefore, the overall time complexity is **O(n)**.

### Storage Complexity

The code creates two string copies of the integer: one for the original string and one for the reversed string. Each string requires O(n) space, where n is the number of digits. Thus, the storage (space) complexity is **O(n)**.

```Python
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
```