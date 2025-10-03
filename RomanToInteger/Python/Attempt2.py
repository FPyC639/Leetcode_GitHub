class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integer values
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate from right to left
        for char in reversed(s):
            curr_value = values[char]
            if curr_value < prev_value:
                total -= curr_value  # subtract if smaller before larger
            else:
                total += curr_value  # otherwise add
            prev_value = curr_value
        
        return total
if __name__ == "__main__":
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))