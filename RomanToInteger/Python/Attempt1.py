class Solution:
    def romanToInt(self, s: str) -> int:
        s, total = self.subtractivepairs(s)
        funcs = [self.countI(s),
        self.countV(s), self.countX(s), self.countL(s),
        self.countC(s), self.countD(s), self.countM(s)]
        total += sum(funcs)
        return total
        
    def subtractivepairs(self, s:str) -> list:
        total = 0
        total += s.count("IV") * 4
        total += s.count("IX") * 9
        total += s.count("XL") * 40
        total += s.count("XC") * 90
        total += s.count("CD") * 400
        total += s.count("CM") * 900

        # Remove subtractive pairs so they’re not double-counted
        for pair in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            s = s.replace(pair, "")
        return s, total
    def countI(self, s:str) -> int:
        return s.count("I") * 1
    def countV(self, s:str) -> int:
        return s.count("V") * 5
    def countX(self, s:str) -> int:
        return s.count("X") * 10
    def countL(self, s:str) -> int:
        return s.count("L") * 50
    def countC(self, s:str) -> int:
        return s.count("C") * 100
    def countD(self, s:str) -> int:
        return s.count("D") * 500
    def countM(self, s:str) -> int:
        return s.count("M") * 1000
if __name__ == "__main__":
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))