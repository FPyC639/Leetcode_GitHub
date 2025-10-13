class Solution:
    def __init__(self):
        self.c = 0
    def func(self,x: str) -> int:
        print(int(x,2))
        return int(x,2)
    def func2(self,x: int) -> int:
        self.c = self.c + x
        return self.c
    def func3(self,x: int) -> int:
        value = self.func2(self.func(x))
        return value
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(list(map(self.func3, [a, b]))[-1]))[2:]