### Complexity Analysis

- **Time Complexity:**  
    The algorithm compares each character of each string up to the length of the shortest string. If there are `n` strings and the shortest string has length `m`, the time complexity is **O(n * m)**.

- **Space Complexity:**  
    The algorithm uses a variable to store the prefix, which in the worst case is of length `m`. Thus, the space complexity is **O(m)**.

```Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        # Enumerate over character positions (zip stops at shortest string)
        for i, chars in enumerate(zip(*strs)):
            # Turn tuple of characters into a set
            if len(set(chars)) == 1:  
                prefix += chars[0]  # All same, keep it
            else:
                break  # stop at first mismatch

        return prefix
    ```