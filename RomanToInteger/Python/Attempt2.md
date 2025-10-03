### Space and Time Complexity

- **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. The algorithm iterates through each character of the string once.
- **Space Complexity:** $O(1)$. The space used by the `values` dictionary is constant and does not depend on the input size.

```Python
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
```