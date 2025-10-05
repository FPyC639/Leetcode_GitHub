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

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interstellar", "internet", "internal"], "inte"),
        (["a"], "a"),
        ([], ""),
        (["prefix", "prefixes", "prefixed"], "prefix"),
        (["same", "same", "same"], "same"),
        (["abc", "ab", "a"], "a"),
    ]

    for i, (strs, expected) in enumerate(test_cases):
        result = solution.longestCommonPrefix(strs)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")